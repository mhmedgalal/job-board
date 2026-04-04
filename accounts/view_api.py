from datetime import timedelta

from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Profile
from .serializers import SingUpSerializer, userSerializers


def get_current_host(request):
    protocol = 'https' if request.is_secure() else 'http'
    return f'{protocol}://{request.get_host()}/'


class ForgotPasswordThrottle(AnonRateThrottle):
    scope = 'forgot_password'


@api_view(['POST'])
def register(request):
    serializer = SingUpSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {'details': 'Your account registered successfully'},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    refresh_token = request.data.get('refresh')
    if not refresh_token:
        return Response({'detail': 'refresh token required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        token = RefreshToken(refresh_token)
        token.blacklist()
    except Exception:
        return Response({'detail': 'invalid refresh token'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'detail': 'logged out'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    return Response(userSerializers(request.user, many=False).data)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_user(request):
    user = request.user
    data = request.data

    new_email = data.get('email')
    if new_email and User.objects.filter(email__iexact=new_email).exclude(id=user.id).exists():
        return Response({'email': ['This email is already in use.']}, status=status.HTTP_400_BAD_REQUEST)

    new_username = data.get('username')
    if new_username and User.objects.filter(username__iexact=new_username).exclude(id=user.id).exists():
        return Response({'username': ['This username is already in use.']}, status=status.HTTP_400_BAD_REQUEST)

    for field in ('first_name', 'last_name', 'email', 'username'):
        if field in data:
            setattr(user, field, data[field])

    if data.get('password'):
        return Response(
            {'password': ['Please use the change_password endpoint to update your password.']},
            status=status.HTTP_400_BAD_REQUEST,
        )

    user.save()
    return Response(userSerializers(user).data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    old_password = request.data.get('old_password')
    new_password = request.data.get('new_password')
    confirm_password = request.data.get('confirm_password')

    if not old_password or not new_password or not confirm_password:
        return Response({'error': 'All fields are required.'}, status=status.HTTP_400_BAD_REQUEST)
    if new_password != confirm_password:
        return Response({'error': 'Passwords are not the same'}, status=status.HTTP_400_BAD_REQUEST)
    if len(new_password) < 8:
        return Response(
            {'error': 'Password must be at least 8 characters long.'},
            status=status.HTTP_400_BAD_REQUEST,
        )
    if not request.user.check_password(old_password):
        return Response({'error': 'Old password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)

    request.user.set_password(new_password)
    request.user.save()
    return Response({'details': 'Password changed successfully.'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_avatar(request):
    file_obj = request.FILES.get('image')
    if not file_obj:
        return Response(
            {'error': 'image file is required with key "image"'},
            status=status.HTTP_400_BAD_REQUEST,
        )

    content_type = getattr(file_obj, 'content_type', '')
    if content_type and not content_type.startswith('image/'):
        return Response({'error': 'Only image files are allowed.'}, status=status.HTTP_400_BAD_REQUEST)

    profile, _ = Profile.objects.get_or_create(user=request.user)
    profile.image = file_obj
    profile.save()
    return Response({'details': 'Avatar uploaded successfully.'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@throttle_classes([ForgotPasswordThrottle])
def forgot_password(request):
    email = request.data.get('email', '').strip().lower()
    if not email:
        return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.filter(email__iexact=email).first()
    if not user:
        return Response(
            {'details': 'If this email exists, a password reset link has been sent.'},
            status=status.HTTP_200_OK,
        )

    profile, _ = Profile.objects.get_or_create(user=user)
    token = get_random_string(40)
    expire_date = timezone.now() + timedelta(minutes=10)

    profile.reset_password_token = token
    profile.reset_password_expires = expire_date
    profile.save(update_fields=['reset_password_token', 'reset_password_expires'])

    link = f"{get_current_host(request)}api/reset-password/{token}/"
    body = f'Your reset password link is: {link}\nThis link will expire in 10 minutes.'

    try:
        send_mail(
            subject='Password Reset Request',
            message=body,
            from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@example.com'),
            recipient_list=[email],
            fail_silently=False,
        )
    except Exception:
        return Response(
            {'error': 'Failed to send email - check email settings.'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return Response(
        {'details': 'If this email exists, a password reset link has been sent.'},
        status=status.HTTP_200_OK,
    )


@api_view(['POST'])
def reset_password(request, token):
    profile = get_object_or_404(Profile, reset_password_token=token)

    if not profile.reset_password_expires or profile.reset_password_expires < timezone.now():
        return Response({'error': 'Token is expired'}, status=status.HTTP_400_BAD_REQUEST)

    password = request.data.get('password', '')
    confirm_password = request.data.get('confirm_password', '')

    if password != confirm_password:
        return Response({'error': 'Passwords are not the same'}, status=status.HTTP_400_BAD_REQUEST)

    if len(password) < 8:
        return Response(
            {'error': 'Password must be at least 8 characters long.'},
            status=status.HTTP_400_BAD_REQUEST,
        )

    user = profile.user
    user.set_password(password)
    user.save()

    profile.reset_password_token = None
    profile.reset_password_expires = None
    profile.save(update_fields=['reset_password_token', 'reset_password_expires'])

    return Response({'details': 'Password reset done'}, status=status.HTTP_200_OK)

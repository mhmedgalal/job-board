# accounts/view_api.py
from datetime import timedelta
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings
from .serializers import SingUpSerializer, userSerializers
from .models import Profile   # أضفت الاستيراد من أجل get_or_create
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.files.uploadedfile import InMemoryUploadedFile


# ---------- helpers ----------
def get_current_host(request):
    protocol = 'https' if request.is_secure() else 'http'
    return f"{protocol}://{request.get_host()}/"


class LoginThrottle(UserRateThrottle):
    scope = 'login'


class ForgotPasswordThrottle(AnonRateThrottle):
    scope = 'forgot_password'


# ---------- المستخدم ----------
@api_view(['POST'])
def register(request):
    data = request.data
    ser = SingUpSerializer(data=data)
    if ser.is_valid():
        if User.objects.filter(email=data['email']).exists():
            return Response({'error': 'This email already exists!'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(
            username=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password=make_password(data['password'])
        )
        return Response({'details': 'Your account registered successfully'},
                        status=status.HTTP_201_CREATED)
    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    """Blacklist refresh token on logout."""
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


#تعديل البروفايل 
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_user(request):
    user = request.user
    data = request.data          
    for field in ('first_name', 'last_name', 'email', 'username'):
        if field in data:
            setattr(user, field, data[field])

    if data.get('password'):
        user.password = make_password(data['password'])

    user.save()
    return Response(userSerializers(user).data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    data = request.data
    old_password = data.get('old_password')
    new_password = data.get('new_password')
    confirm_password = data.get('confirm_password')

    if not old_password or not new_password or not confirm_password:
        return Response({'error': 'All fields are required.'}, status=status.HTTP_400_BAD_REQUEST)
    if new_password != confirm_password:
        return Response({'error': 'Passwords are not the same'}, status=status.HTTP_400_BAD_REQUEST)
    if len(new_password) < 8:
        return Response({'error': 'Password must be at least 8 characters long.'}, status=status.HTTP_400_BAD_REQUEST)
    if not request.user.check_password(old_password):
        return Response({'error': 'Old password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)

    request.user.password = make_password(new_password)
    request.user.save()
    return Response({'details': 'Password changed successfully.'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_avatar(request):
    file_obj = request.FILES.get('image')
    if not file_obj:
        return Response({'error': 'image file is required with key "image"'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        profile = request.user.profile
    except Exception:
        profile = Profile(user=request.user)
    profile.image = file_obj
    profile.save()
    return Response({'details': 'Avatar uploaded successfully.'}, status=status.HTTP_200_OK)

# ---------- إعادة تعيين كلمة المرور ----------
@api_view(['POST'])
@throttle_classes([ForgotPasswordThrottle])
def forgot_password(request):
    """
    إنشاء رمز استعادة (token) وإرساله بالبريد.
    التعديل الوحيد: التأكد من وجود Profile أو إنشاؤه تلقائياً.
    """
    email = request.data.get('email')
    if not email:
        return Response({'error': 'Email is required'},
                        status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(User, email=email)

    # >>> التعديل: خطوة واحدة مضمونة <<
    try:
        profile = user.profile
    except Exception:
        profile = Profile(user=user)
        profile.save()

    token = get_random_string(40)
    expire_date = timezone.now() + timedelta(minutes=10)

    setattr(profile, 'reset_password_token', token)
    setattr(profile, 'reset_password_expires', expire_date)
    profile.save()

    link = f"{get_current_host(request)}api/reset-password/{token}/"
    body = (f"Your reset password link is: {link}\n"
            "This link will expire in 10 minutes.")

    try:
        send_mail(subject='Password Reset Request',
                  message=body,
                  from_email=getattr(settings, 'DEFAULT_FROM_EMAIL',
                                     'noreply@example.com'),
                  recipient_list=[email],
                  fail_silently=False)
    except Exception as e:
        import traceback
        traceback.print_exc()          # 👈 بيطبّع التفاصيل كاملة
        return Response(
            {'error': 'Failed to send email - check email settings.'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
    return Response({'details': f'Password reset link sent to {email}'},
                    status=status.HTTP_200_OK)


@api_view(['POST'])
def reset_password(request, token):
    """
    استلام كلمة المرور الجديدة والتحقق من صلاحية الرمز.
    لم يُغيَّر شيء هنا باستثناء شطب السطر الخاطئ (user.profile) لأنّ
    الاستعلام profile__reset_password_token يُعطينا المستخدم مباشرةً.
    """
    data = request.data
    user = get_object_or_404(User, profile__reset_password_token=token)
    profile = user.profile          # هنا مضمون وجوده بفضل get_or_create أعلاه

    if not profile.reset_password_expires or profile.reset_password_expires < timezone.now():
        return Response({'error': 'Token is expired'},
                        status=status.HTTP_400_BAD_REQUEST)

    if data.get('password') != data.get('confirm_password'):
        return Response({'error': 'Passwords are not the same'},
                        status=status.HTTP_400_BAD_REQUEST)

    if len(data.get('password', '')) < 8:
        return Response({'error': 'Password must be at least 8 characters long.'},
                        status=status.HTTP_400_BAD_REQUEST)

    user.password = make_password(data['password'])
    profile.reset_password_token = None   # None أفضل من ''
    profile.reset_password_expires = None
    profile.save()
    user.save()

    return Response({'details': 'Password reset done'},
                    status=status.HTTP_200_OK)
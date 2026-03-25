from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Security Fix: Send contact form email to site admin, not the user-supplied email
        # The user's email is included in the body for replying
        full_message = f"From: {email}\n\nMessage:\n{message}"

        send_mail(
            subject,
            full_message,
            getattr(settings, 'DEFAULT_FROM_EMAIL', settings.EMAIL_HOST_USER),
            [settings.EMAIL_HOST_USER], # send to site admin
            fail_silently=False,
        )
    return render(request, 'contact/contact.html')
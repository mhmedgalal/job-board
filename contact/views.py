from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # 🛡️ Security Fix: Prevent Open Email Relay
        # Forward the message to the admin/app owner instead of the user-provided email
        admin_email = getattr(settings, 'DEFAULT_FROM_EMAIL', settings.EMAIL_HOST_USER)
        full_message = f"Message from: {email}\n\n{message}"

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            [admin_email],
            fail_silently=False,
        )
    return render(request, 'contact/contact.html')
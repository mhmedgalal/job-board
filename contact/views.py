from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Security: Prevent Open Mail Relay vulnerability by sending the message to admin instead of user email
        full_message = f"Message from: {email}\n\n{message}"
        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            [getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@example.com')],
            fail_silently=False,
        )
    return render(request, 'contact/contact.html')
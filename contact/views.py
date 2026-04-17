from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Prevent open relay: send message to admin, not arbitrary user input email
        admin_email = getattr(settings, 'EMAIL_HOST_USER', None) or getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@example.com')
        full_message = f"Message from {email}:\n\n{message}"

        send_mail(
            subject,
            full_message,
            admin_email,
            [admin_email],
            fail_silently=False,
        )
    return render(request, 'contact/contact.html')
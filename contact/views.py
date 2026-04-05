from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', 'No Subject')
        email = request.POST.get('email', 'No Email Provided')
        message = request.POST.get('message', '')

        # Protect against Arbitrary Email Sending / Open Relay
        full_message = f"Message from {email}:\n\n{message}"
        admin_email = getattr(settings, 'DEFAULT_FROM_EMAIL', 'admin@example.com')

        send_mail(
            f"Contact Form: {subject}",
            full_message,
            admin_email,
            [admin_email],
            fail_silently=False,
        )
    return render(request, 'contact/contact.html')
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Prevent open email relay by sending to the site admin instead of user input
        full_message = f"Message from: {email}\n\n{message}"
        recipient = getattr(settings, 'DEFAULT_FROM_EMAIL', settings.EMAIL_HOST_USER)
        if not recipient:
            recipient = 'admin@localhost'

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            [recipient],
            fail_silently=False,
        )
    return render(request, 'contact/contact.html')
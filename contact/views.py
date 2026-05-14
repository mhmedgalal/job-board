from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')

        formatted_message = f"From: {email}\n\n{message}"
        recipient = getattr(settings, 'DEFAULT_FROM_EMAIL', 'admin@example.com')

        send_mail(
            subject,
            formatted_message,
            settings.EMAIL_HOST_USER,
            [recipient],
            fail_silently=False,
        )
    return render(request, 'contact/contact.html')
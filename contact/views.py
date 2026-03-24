from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        full_message = f"From: {email}\n\n{message}"
        # Prevent open relay by sending to a known internal address rather than the user-provided one.
        recipient = getattr(settings, 'DEFAULT_FROM_EMAIL', settings.EMAIL_HOST_USER)
        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            [recipient],
            fail_silently=False,
        )
    return render(request, 'contact/contact.html')
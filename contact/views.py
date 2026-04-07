from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if subject and email and message:
            full_message = f"From: {email}\n\n{message}"
            recipient = getattr(settings, 'DEFAULT_FROM_EMAIL', settings.EMAIL_HOST_USER)
            try:
                send_mail(
                    subject,
                    full_message,
                    settings.EMAIL_HOST_USER,
                    [recipient],
                    fail_silently=False,
                )
            except Exception:
                # Fail securely without leaking stack traces
                pass

    return render(request, 'contact/contact.html')
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        # Basic validation
        if subject and email and message:
            # Prevent header injection by removing newlines from subject
            subject = ''.join(subject.splitlines())

            # Format message to include sender info
            full_message = f"From: {email}\n\n{message}"

            # Send to admin/configured recipient instead of the user
            recipient_email = getattr(settings, 'DEFAULT_FROM_EMAIL', settings.EMAIL_HOST_USER)

            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,
                [recipient_email],
                fail_silently=False,
            )
    return render(request, 'contact/contact.html')
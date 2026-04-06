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

        recipient = settings.EMAIL_HOST_USER if settings.EMAIL_HOST_USER else 'admin@example.com'
        from_email = settings.DEFAULT_FROM_EMAIL

        send_mail(
            subject,
            full_message,
            from_email,
            [recipient],
            fail_silently=False,
        )
    return render(request, 'contact/contact.html')
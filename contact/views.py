from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # 🛡️ Sentinel: Fix Open Mail Relay
        # Send to the admin/configured address instead of the user-provided one
        admin_email = getattr(settings, 'DEFAULT_FROM_EMAIL', settings.EMAIL_HOST_USER)
        body = f"Message from: {email}\n\n{message}"

        if admin_email:
            send_mail(
                subject,
                body,
                admin_email,
                [admin_email],
                fail_silently=False,
            )
    return render(request, 'contact/contact.html')
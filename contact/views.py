from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # 🛡️ Sentinel: Fix Open Mail Relay / Spam injection
        # Prevents attackers from using this form to send emails to arbitrary addresses.
        # Send to the admin, not to the user-provided email address.
        admin_email = getattr(settings, 'DEFAULT_FROM_EMAIL', getattr(settings, 'EMAIL_HOST_USER', 'admin@example.com'))
        formatted_message = f"Message from: {email}\n\n{message}"

        send_mail(
            subject=f"Contact Form: {subject}",
            message=formatted_message,
            from_email=admin_email,
            recipient_list=[admin_email],
            fail_silently=False,
        )
    return render(request, 'contact/contact.html')
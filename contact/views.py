from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Format the message to include the sender's email
        full_message = f"Message from {email}:\n\n{message}"

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER], # Send to admin, not the user-provided email
            fail_silently=False,
        )
    return render(request, 'contact/contact.html')
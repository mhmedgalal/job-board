from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Format message to include sender's email
        formatted_message = f"Message from: {email}\n\n{message}"

        send_mail(
            subject,
            formatted_message,
            settings.EMAIL_HOST_USER,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
    return render(request, 'contact/contact.html')
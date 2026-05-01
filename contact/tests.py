from django.test import TestCase
from django.urls import reverse
from django.core import mail
from django.conf import settings

class ContactFormTests(TestCase):
    def test_contact_form_sends_email_to_admin(self):
        url = reverse('contact:contact')
        data = {
            'subject': 'Test Subject',
            'email': 'hacker@example.com',
            'message': 'Test Message'
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)

        # Check that one message was sent
        self.assertEqual(len(mail.outbox), 1)

        # Check that the email was sent to the admin, not the user
        admin_email = getattr(settings, 'DEFAULT_FROM_EMAIL', settings.EMAIL_HOST_USER)
        self.assertEqual(mail.outbox[0].to, [admin_email])

        # Check that the user's email is in the body
        self.assertIn('hacker@example.com', mail.outbox[0].body)
        self.assertIn('Test Message', mail.outbox[0].body)

from django.test import TestCase
from django.core import mail
from django.urls import reverse
from django.conf import settings

from django.test import override_settings

class ContactViewTest(TestCase):
    @override_settings(EMAIL_HOST_USER='admin@example.com')
    def test_contact_form_sends_email_to_admin(self):
        url = reverse('contact:contact')
        data = {
            'subject': 'Test Subject',
            'email': 'user@example.com',
            'message': 'This is a test message.'
        }

        response = self.client.post(url, data)

        # Check that one message has been sent
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject is correct
        self.assertEqual(mail.outbox[0].subject, 'Test Subject')

        # Verify that the message goes to the admin, NOT the user
        self.assertEqual(mail.outbox[0].to, [settings.EMAIL_HOST_USER])

        # Verify that the message body contains both the user email and message
        self.assertIn('Message from: user@example.com', mail.outbox[0].body)
        self.assertIn('This is a test message.', mail.outbox[0].body)

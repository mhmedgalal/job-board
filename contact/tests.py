from django.test import TestCase
from django.urls import reverse
from django.core import mail
from django.conf import settings

class ContactViewTest(TestCase):
    def test_contact_form_sends_email_to_admin(self):
        # Setup settings for test
        settings.EMAIL_HOST_USER = 'admin@example.com'

        response = self.client.post(reverse('contact:contact'), {
            'subject': 'Test Subject',
            'email': 'hacker@evil.com',
            'message': 'Test Message'
        })

        self.assertEqual(response.status_code, 200)

        # Verify an email was sent
        self.assertEqual(len(mail.outbox), 1)

        # Verify the email was sent to the admin, not the user
        sent_email = mail.outbox[0]
        self.assertEqual(sent_email.to, ['admin@example.com'])
        self.assertNotIn('hacker@evil.com', sent_email.to)

        # Verify the user's email is in the message body
        self.assertIn('Message from: hacker@evil.com', sent_email.body)
        self.assertIn('Test Message', sent_email.body)
        self.assertEqual(sent_email.subject, 'Test Subject')

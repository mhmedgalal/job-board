from django.test import TestCase
from django.urls import reverse
from django.core import mail
from django.conf import settings

class ContactTest(TestCase):
    def test_contact_form_sends_email_to_admin(self):
        """
        Test that submitting the contact form sends the email to the admin
        (EMAIL_HOST_USER) and not to the email provided by the user.
        """
        user_email = 'hacker@example.com'
        data = {
            'subject': 'Test Subject',
            'email': user_email,
            'message': 'Test message content.'
        }

        # Ensure outbox is empty
        self.assertEqual(len(mail.outbox), 0)

        # Submit the form
        response = self.client.post(reverse('contact:contact'), data)

        # Verify the view returns a 200 (or redirect if we decide to change the view later, but currently it returns render)
        self.assertEqual(response.status_code, 200)

        # Ensure 1 email was sent
        self.assertEqual(len(mail.outbox), 1)

        sent_email = mail.outbox[0]

        # The email should be sent TO the admin, NOT the user_email
        expected_recipient = settings.EMAIL_HOST_USER if settings.EMAIL_HOST_USER else 'admin@example.com'
        self.assertIn(expected_recipient, sent_email.to)
        self.assertNotIn(user_email, sent_email.to)

        # The user_email should be in the body of the email
        self.assertIn(user_email, sent_email.body)
        self.assertIn('Test message content.', sent_email.body)

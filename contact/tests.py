from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from django.conf import settings

class ContactFormSecurityTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_contact_form_sends_to_admin_not_submitter(self):
        """
        Test that submitting the contact form sends the email to the DEFAULT_FROM_EMAIL
        (the admin) and NOT to the email address provided in the form, preventing
        an open email relay vulnerability.
        """
        url = reverse('contact:contact')  # Adjust namespace/name if necessary

        test_subject = 'Test Subject'
        test_email = 'attacker@example.com'
        test_message = 'This is a test message.'

        from django.test import RequestFactory
        from contact.views import contact

        factory = RequestFactory()
        request = factory.post(url, {
            'subject': test_subject,
            'email': test_email,
            'message': test_message,
        })

        # Submit the form via the view directly to bypass template rendering errors
        response = contact(request)

        # Verify the response is successful (e.g., 200 OK)
        self.assertEqual(response.status_code, 200)

        # Verify exactly one email was sent
        self.assertEqual(len(mail.outbox), 1)

        sent_email = mail.outbox[0]

        # Verify the email subject
        self.assertEqual(sent_email.subject, test_subject)

        # Verify the email body contains the submitter's email and message
        self.assertIn(test_email, sent_email.body)
        self.assertIn(test_message, sent_email.body)

        # CRITICAL SECURITY CHECK: Verify the email was sent TO the admin, NOT the submitter
        admin_email = getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@example.com')
        self.assertEqual(sent_email.to, [admin_email])
        self.assertNotIn(test_email, sent_email.to)

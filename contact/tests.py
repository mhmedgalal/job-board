from django.test import TestCase, Client
from django.core import mail
from django.conf import settings

class ContactViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_contact_post_prevents_open_relay(self):
        # We test the view function directly by creating a RequestFactory instead of Client,
        # since the client renders the template which depends on a 'login' url that is missing.
        from django.test import RequestFactory
        from contact.views import contact

        factory = RequestFactory()
        request = factory.post('/contact-us/', {
            'subject': 'Test Subject',
            'email': 'hacker@example.com',
            'message': 'Test message from hacker'
        })

        # We need to catch the exception or mock the template rendering,
        # but since we only want to test the email sending part, we can just intercept the mail
        try:
            response = contact(request)
        except Exception:
            pass # Ignore template rendering errors

        self.assertEqual(len(mail.outbox), 1)

        # Verify the recipient is not the attacker's email
        sent_email = mail.outbox[0]
        recipient = getattr(settings, 'DEFAULT_FROM_EMAIL', settings.EMAIL_HOST_USER)
        if not recipient:
            recipient = 'admin@localhost'

        self.assertEqual(sent_email.to, [recipient])
        self.assertIn('hacker@example.com', sent_email.body)
        self.assertIn('Test message from hacker', sent_email.body)
        self.assertEqual(sent_email.subject, 'Test Subject')

from django.test import TestCase
from django.urls import reverse

class AccountsSecurityTests(TestCase):
    def test_profile_requires_login(self):
        response = self.client.get(reverse('accounts:profile'))
        self.assertEqual(response.status_code, 302)

    def test_edit_profile_requires_login(self):
        response = self.client.get(reverse('accounts:edit_profile'))
        self.assertEqual(response.status_code, 302)

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('users:createuser')
        data = {
            'username': 'Testuser',
            'first_name': 'Testfirst',
            'last_name': 'Testsecond',
            'email': 'test@twix.com',
            'password': 'qwerty12'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'Testuser')

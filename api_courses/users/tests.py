import json


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from django.contrib.auth.models import User


class AccountTests(APITestCase):
    @classmethod
    def setUpTestData(cls):

        cls.url = reverse('users:createuser')

        cls.valid_data = {
            'username': 'Testuser',
            'first_name': 'Testfirst',
            'last_name': 'Testsecond',
            'email': 'test@bounty.com',
            'password': 'qwerty123',
            'confirm_password': 'qwerty321',
        }

        cls.pass_not_match = {
            'username': 'username',
            'password': 'qwerty123',
            'confirm_password': 'qwerty321',
            'email': 'test@sneakers.com'
        }

        cls.email_exists = {
            'username': 'username',
            'password': 'qwerty123',
            'confirm_password': 'qwerty123',
            'email': 'test@twix.com'
        }

        cls.client = APIClient()

    def test_create_account(self):
        """Ensure we can create a new account object."""
        response = self.client.post(self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_registration_invalid_data_passwords_doesnt_match(self):
        """Make sure that the object is not created if the passwords do not match"""
        response = self.client.post(self.url, self.pass_not_match, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



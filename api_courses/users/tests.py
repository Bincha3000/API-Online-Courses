import json

from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, APIClient, force_authenticate
from django.contrib.auth.models import User


class AccountTests(APITestCase):

    @classmethod
    def setUpTestData(cls):

        cls.signup_url = reverse('users:createuser')
        cls.login_url = reverse('users:login')


        cls.signup_valid_data = {
            'username': 'Testuser',
            'first_name': 'Testfirst',
            'last_name': 'Testsecond',
            'email': 'test@bounty.com',
            'password': 'qwerty123',
        }

        cls.signup_not_valid_email = {
            'username': 'Testuser',
            'first_name': 'Testfirst',
            'last_name': 'Testsecond',
            'password': 'qwerty123',
            'email': 'testsneakers.com'
        }

        cls.login_valid_data = {
            'username': 'Testuser',
            'password': 'qwerty123',
        }

        cls.client = APIClient()

    def test_create_account(self):
        """Make sure we can create a new account object."""
        response = self.client.post(self.signup_url, self.signup_valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_account_not_valid_email(self):
        """Make sure that the object is not created if email not valid"""
        response = self.client.post(self.signup_url, self.signup_not_valid_email, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_login(self):
        """Test that the user can login"""
        self.client.post(self.signup_url, self.signup_valid_data, format='json')
        response = self.client.post(self.login_url, self.login_valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_login_response_token(self):
        """Check that when login, the user in the response receives a token"""
        self.client.post(self.signup_url, self.signup_valid_data, format='json')
        response = self.client.post(self.login_url, self.login_valid_data, format='json')
        token = Token.objects.get(user__username=self.login_valid_data['username'])
        self.assertEqual(response.data['token'], token.key)


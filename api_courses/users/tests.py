import json
from django.test import TestCase
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User



CREATE_USER_URL = reverse('users:createuser')
LOGIN_USER_URL = reverse('users:login')
LOGOUT_USER_URL = reverse('users:logout')


class AccountTests(TestCase):


    def setUp(self):

        self.client = APIClient()

        self.signup_valid_data = {
            'username': 'Testuser',
            'first_name': 'Testfirst',
            'last_name': 'Testsecond',
            'email': 'test@bounty.com',
            'password': 'qwerty123',
        }

        self.signup_password_too_short = {
            'username': 'Testuser',
            'first_name': 'Testfirst',
            'last_name': 'Testsecond',
            'password': 'qw3',
            'email': 'testsneakers.com'
        }

        self.signup_not_valid_email = {
            'username': 'Testuser',
            'first_name': 'Testfirst',
            'last_name': 'Testsecond',
            'password': 'qwerty123',
            'email': 'testsneakers.com'
        }

        self.login_valid_data = {
            'username': 'Testuser',
            'password': 'qwerty123',
        }

        self.login_invalid_data = {
            'username': 'Testuser',
            'password': 'qwerty321',
        }



    def test_create_user_success(self):
        res = self.client.post(CREATE_USER_URL, self.signup_valid_data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_user_not_success(self):
        res = self.client.post(CREATE_USER_URL, self.signup_not_valid_email)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_short_password(self):
        res = self.client.post(CREATE_USER_URL, self.signup_password_too_short)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_for_user(self):
        res = self.client.post(CREATE_USER_URL, self.signup_valid_data)
        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        self.client.post(CREATE_USER_URL, self.signup_valid_data)
        res = self.client.post(LOGIN_USER_URL, self.login_valid_data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_login_invalid_data(self):
        self.client.post(CREATE_USER_URL, self.signup_valid_data)
        res = self.client.post(LOGIN_USER_URL, self.login_invalid_data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_when_user_login(self):
        self.client.post(CREATE_USER_URL, self.signup_valid_data)
        res = self.client.post(LOGIN_USER_URL, self.login_valid_data)
        self.assertIn('token', res.data)

    def test_user_logout(self):
        user = self.client.post(CREATE_USER_URL, self.signup_valid_data)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + user.data['token'])
        res = self.client.get(LOGOUT_USER_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

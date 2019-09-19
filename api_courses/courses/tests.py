from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core import management
from courses.tasks import notification_courses_email, registration_email
from rest_framework import status
from rest_framework.test import APIClient

from courses.models import Category, Course, Teacher, Profile


CREATE_USER_URL = reverse('users:createuser')

ALL_COURSES_URL = reverse('courses:courses')
ONE_COURSE_URL = reverse('courses:course',kwargs={'pk': 1})
CATEGORIES_COURSES_URL = reverse('courses:categories')
TEACHERS_URL = reverse('courses:teachers')
PROFILE_URL = reverse('courses:profile')
ENROLLMENT_COURSE_URL = reverse('courses:enrollment')

class WalletApiTests(TestCase):

    def setUp(self):
        management.call_command('generate_categories')
        management.call_command('generate_courses')
        management.call_command('generate_lessons')
        context_for_user = {
            'username': 'Testuser',
            'first_name': 'Testfirst',
            'last_name': 'Testsecond',
            'email': 'test@bounty.com',
            'password': 'qwerty123',
        }
        res = self.client.post(CREATE_USER_URL, context_for_user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + res.data['token'])


    def test_courses_view(self):
        res = self.client.get(ALL_COURSES_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_obe_courses_view(self):
        res = self.client.get(ONE_COURSE_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_view_categories(self):
        res = self.client.get(CATEGORIES_COURSES_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_teachers_view(self):
        res = self.client.get(TEACHERS_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_profile_view(self):
        res = self.client.get(PROFILE_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_user_enrollment_course(self):

        context = {
            'pk':'1'
        }
        res = self.client.post(ENROLLMENT_COURSE_URL, context)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

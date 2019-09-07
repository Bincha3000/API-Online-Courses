from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status

from courses.tasks import notification_courses_email
from courses.models import Course, Category, Teacher

from courses.serializers import (
    CourseSerializer,
    CategorySerializer,
    TeacherSerializer,
    UserSerializer
)

from datetime import datetime
from courses.tasks import notification_courses_email
import django_rq


class AllCoursesView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OneCourseView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoriesView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeachersView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        user = request.user
        data = request.data
        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EnrollmentOnCourseView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        user = request.user
        pk = request.data.get('pk')
        course = get_object_or_404(Course, pk=pk)

        if user not in course.student.all():
            course.student.add(user)
            message = {"Сongratulations! You have successfully signed up for the course"}
            return Response(message, status=status.HTTP_201_CREATED)
        else:
            message = {"Looks like you've already been enrolled."}
            return Response(message, status=status.HTTP_304_NOT_MODIFIED)


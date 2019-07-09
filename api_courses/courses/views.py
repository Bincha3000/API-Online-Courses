from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from courses.models import Course, Category, Teacher
from django.contrib.auth.models import User
from courses.serializers import CourseSerializer, CategorySerializer, TeacherSerializer, UserSerializer


class AllCoursesView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = (permissions.AllowAny, )

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class OneCourseView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = (permissions.AllowAny, )

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)


class CategoriesView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = (permissions.AllowAny, )

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class TeachersView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = (permissions.AllowAny, )

    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)


class PersonalArea(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = User.objects.get(username=request.user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
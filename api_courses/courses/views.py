from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from django.contrib.auth.models import User
from courses.models import Course, Category, Teacher, Profile
from courses.serializers import CourseSerializer, CategorySerializer, \
                                TeacherSerializer, UserSerializer, ProfileSerializer


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


class ProfileView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        profile = User.objects.get(username=request.user)
        serializer = UserSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        try:
            profile = User.objects.get(username=request.user)
            serializer = UserSerializer(profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            serializer = UserSerializer(data=param)
            if serializer.is_valid():
                serializer.save(username=request.user)
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
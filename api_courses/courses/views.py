from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from courses.models import Course, Category, Teacher
from courses.serializers import CourseSerializer, CategorySerializer, TeacherSerializer
from django.contrib.auth.mixins import LoginRequiredMixin


class AllCoursesView(LoginRequiredMixin, APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class OneCourseView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)


class CategoriesView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class TeachersView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

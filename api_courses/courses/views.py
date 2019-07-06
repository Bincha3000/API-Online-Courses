from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework import permissions

from courses.models import Course
from courses.serializers import CourseSerializer



class AllCoursesView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        items = Course.objects.all()
        serializer = CourseSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OneCourseView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk):
        item = get_object_or_404(Course, pk=pk)
        print(pk)
        serializer = CourseSerializer(item)
        return Response(serializer.data)


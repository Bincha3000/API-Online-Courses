from rest_framework import serializers
from courses.models import Course, Teacher, Lesson, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title', 'description')


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('id', 'title', 'description', 'course', 'date', 'duration', 'homework', 'finished')


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ('id', 'first_name', 'last_name', 'info')


class CourseSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    lessons = LessonSerializer(many=True)
    teacher = TeacherSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'category', 'title', 'short_description', 'long_description', 'price', 'date_start', 'date_end', 'teacher', 'lessons')

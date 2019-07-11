from rest_framework import serializers
from django.contrib.auth.models import User

from courses.models import Course, Teacher, Lesson, Category, Profile


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


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id', 'bio', 'location', 'birth_date')


class UserSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile')

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()

        profile.bio = profile_data.get('bio', profile.bio)
        profile.location = profile_data.get('location', profile.location)
        profile.birth_date = profile_data.get('birth_date', profile.birth_date)

        profile.save()

        return instance
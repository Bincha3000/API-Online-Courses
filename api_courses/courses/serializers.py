from rest_framework import serializers
from courses.models import Course, Teacher, Lesson, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title', 'description')


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('id', 'title', 'description', 'date', 'homework', 'course')


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ('id', 'first_name', 'last_name', 'info')


class CourseSerializer(serializers.ModelSerializer):
    lessons = serializers.StringRelatedField(many=True)
    teacher = serializers.StringRelatedField(many=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'short_description', 'long_description', 'price', 'date_start', 'date_end', 'teacher', 'lessons')




# class CourseSignupSerializer(ModelSerializer):
#     class Meta:
#         model = Course
#         fields = ('id', 'title', 'students')
#         extra_kwargs = {'students': {'write_only': True}}

#     def update(self, instance, validated_data):
#         user = self.context['request'].user
#         if user not in instance.students.all():
#             instance.students.add(user)
#         return instance
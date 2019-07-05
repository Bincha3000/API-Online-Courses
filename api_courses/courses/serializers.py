from rest_framework.serializers import ModelSerializer
from courses.models import Course, Teacher, Lesson


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('id', 'title', 'description', 'date', 'homework', 'course')


class CourseSerializer(ModelSerializer):
    lessons = serializers.StringRelatedField(many=True)
    teachers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'price', 'date_start', 'duration', 'teachers', 'lessons')


class TeacherSerializer(ModelSerializer):

    class Meta:
        model = Teacher
        fields = ('id', 'first_name', 'last_name', 'about')


class CourseSignupSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'students')
        extra_kwargs = {'students': {'write_only': True}}

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user not in instance.students.all():
            instance.students.add(user)
        return instance
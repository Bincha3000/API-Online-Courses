from django.core.management.base import BaseCommand
from django.utils import timezone
from courses.models import (
    Course,
    Lesson,
)

from faker import Faker


class Command(BaseCommand):

    def generate(self, *args, **kwargs):

        fake = Faker()
        course = Course.objects.values_list('id', flat=True)

        for i in range(5):
            Lesson.objects.create(
                title=fake.job(),
                course_id=fake.random.choice(course),
                description=fake.text(max_nb_chars=50), 
                date=timezone.now(),
                duration=90,
                homework=fake.text(max_nb_chars=50),
            )

    def handle(self, *args, **kwargs):
        self.generate()

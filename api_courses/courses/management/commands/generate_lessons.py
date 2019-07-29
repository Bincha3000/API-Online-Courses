from django.core.management.base import BaseCommand

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
                date=fake.date_time_this_year(before_now=False, after_now=True, tzinfo=None),
                duration=90,
                homework=fake.text(max_nb_chars=50),
                finished=False,
            )

    def handle(self, *args, **kwargs):
        self.generate()

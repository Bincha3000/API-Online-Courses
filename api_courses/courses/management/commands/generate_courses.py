from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from courses.models import (
    Course,
    Category,
    Teacher
)

from faker import Faker
import random


class Command(BaseCommand):

    def generate(self, *args, **kwargs):

        fake = Faker()
        categories = Category.objects.values_list('id', flat=True)
        teacher = list(Teacher.objects.values_list('id', flat=True))
        student = list(User.objects.values_list('id', flat=True))

        for i in range(5):
            course = Course.objects.create(
                title=fake.job(),
                category_id=random.choice(categories),
                description=fake.text(max_nb_chars=200),
                price=random.random() * 10000,
                date_start=fake.date_this_month(before_today=True, after_today=False),
                date_end=fake.date_this_year(before_today=True, after_today=False),
            )
            course.teacher.add(
                *random.sample(teacher, random.randint(0, len(teacher)))
            )
            course.student.add(
                *random.sample(student, random.randint(0, len(student)))
            )

    def handle(self, *args, **kwargs):
        self.generate()

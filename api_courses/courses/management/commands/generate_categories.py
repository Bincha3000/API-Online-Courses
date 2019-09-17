from django.core.management.base import BaseCommand
from courses.models import Category

from faker import Faker


class Command(BaseCommand):

    def generate(self, *args, **kwargs):

        fake = Faker()


        for i in range(5):
            categories = Category.objects.create(
                title=fake.job(),
                description=fake.text(max_nb_chars=200),
            )

    def handle(self, *args, **kwargs):
        self.generate()

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from faker import Faker


class Command(BaseCommand):

    def generate(self, *args, **kwargs):

        fake = Faker()

        for i in range(5):
            User.objects.create(
                username=fake.user_name(),
                email=fake.email(),
                password=fake.password(),
            )

    def handle(self, *args, **kwargs):
        self.generate()

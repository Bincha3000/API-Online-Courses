from django.core.management.base import BaseCommand

from courses.tasks import notification_courses_email

from datetime import datetime
import django_rq


class Command(BaseCommand):

    def notification_scheduler_email(self, *args, **kwargs):
        scheduler = django_rq.get_scheduler('default')
        job = scheduler.schedule(
            scheduled_time=datetime.utcnow(),  # Time for first execution, in UTC timezone
            func=notification_courses_email,                     # Function to be queued         # Keyword arguments passed into function when executed
            interval=60,                   # Time before the function is called again, in seconds
            repeat=3,                     # Repeat this number of times (None means repeat forever)          # Arbitrary pickleable data on the job itself
        )

    def handle(self, *args, **kwargs):
        self.notification_scheduler_email()

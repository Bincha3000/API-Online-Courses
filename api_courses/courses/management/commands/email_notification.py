from django.core.management.base import BaseCommand

from courses.tasks import notification_courses_email

from datetime import datetime
import django_rq


class Command(BaseCommand):

    def notification_scheduler_email(self, *args, **kwargs):
        scheduler = django_rq.get_scheduler('default')
        job = scheduler.schedule(
            scheduled_time=datetime.utcnow(),
            func=notification_courses_email,
            interval=60 * 60 * 24,
            repeat=None,
        )

    def handle(self, *args, **kwargs):
        self.notification_scheduler_email()

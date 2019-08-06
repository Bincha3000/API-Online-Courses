from datetime import date, timedelta

from django.core.mail import send_mail
from django.contrib.auth.models import User

from courses.models import Lesson


def registration_email(first_name, last_name, email):
    subject = "Успешная регистрация"
    message = \
        """
            Дорогой(ая) {first_name} {last_name}!
            Поздравляю вы успешно зарегестрировались!
    """.format(first_name=first_name, last_name=last_name)

    send_mail(
        subject=subject,
        message=message,
        from_email="test@bouty.com",
        recipient_list=[email, ],
        fail_silently=False)

    return True


def notification_courses_email(lesson):

    today = date.today()
    tomorrow = today + timedelta(1)
    students = []
    lessons = Lesson.objects.filter(date__range=(today, tomorrow)).all()
    for lesson in lessons:
        students = User.objects.filter(courses=lesson.course).distinct()
        emails = [student.email for student in students]

        subject = 'Напоминание о занятии по теме "{}"'.format(lesson)
        message = \
            """
        Напоминаем о скором проведении урока по теме "{lesson}"!
        Дата и время проведения {date}
        """.format(title=lesson, date=lesson.date)

        send_mail(
            subject=subject,
            message=message,
            from_email="test@bouty.com",
            recipient_list=emails,
            fail_silently=False
        )

        send_email(email)

    return True

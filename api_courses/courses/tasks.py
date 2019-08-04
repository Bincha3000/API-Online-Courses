from datetime import date, timedelta

from django.core.mail import send_mail

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

    lesons = Lesson.objects.filter(start_date=today).all()

    students =

    subject = 'Напоминание о {}'.format(lesson.name)
    message = \
        """
    Напоминаем о скором проведении урока по теме "{title}"!
    Дата и время проведения {date}
    """.format(title=lesson.title, date=lesson.date)

    send_mail(
        subject=subject,
        message=message,
        from_email="test@bouty.com",
        recipient_list=[],
        fail_silently=False
    )

    send_email(email)

    return True

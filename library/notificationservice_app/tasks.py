
from celery import shared_task
from borrowingservice_app.models import Borrowing
from datetime import date
from django.core.mail import send_mail

@shared_task
def check_overdue_books():
    overdue_borrowings = Borrowing.objects.filter(return_date__isnull=True, due_date__lt=date.today())
    for borrowing in overdue_borrowings:
        send_mail(
            'Overdue Book Notification',
            f'Dear {borrowing.member.first_name},\n\nThe book "{borrowing.book.title}" is overdue. Please return it as soon as possible.',
            'umeshtamang129@gmail.com',
            [borrowing.member.email],
            fail_silently=False,
        )
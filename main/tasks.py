import datetime

import fitz
from django.conf import settings

from main.models import User
from project import celery_app
from django.core.mail import send_mail


def generate_email():
    today = datetime.date.today()
    users = User.objects.filter(created_time__gt=today).values('username')
    doc = fitz.open()
    page = doc.new_page()
    shape = page.new_shape()
    t = ' '.join([str(elem) for elem in list(users)])
    shape.insert_text((50, 70), t, fontname="helv", encoding=fitz.TEXT_ENCODING_LATIN)
    shape.commit()
    doc.save(f'new-users-{today}.pdf')


def send_email():
    today = datetime.date.today()
    message = 'this is users'
    # message.attach('Attachment.pdf', f'new-users-{today}.pdf', 'file/pdf')
    send_mail(
        subject='That’s your subject',
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['anotherleili@gmail.com', ],
        auth_user='Login',
        auth_password='Password',
        fail_silently=False,
    )


@celery_app.task()
def daily_users():
    generate_email()
    send_email()

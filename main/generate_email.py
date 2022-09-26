import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

import fitz
from django.conf import settings

from main.models import User
from project import celery_app
from django.core.mail import send_mail

import smtplib
import ssl

from email.mime.multipart import MIMEMultipart


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
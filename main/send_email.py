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


def generate_email_message():
    today = datetime.date.today()
    msg = MIMEMultipart()
    body = '''Hello,
        This is list of new users
        sincerely yours
        '''
    pdfname = f'new-users-{today}.pdf'
    msg.attach(MIMEText(body, 'plain'))
    binary_pdf = open(pdfname, 'rb')
    payload = MIMEBase('application', 'octate-stream', Name=pdfname)
    payload.set_payload((binary_pdf).read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
    msg.attach(payload)
    text = msg.as_string()
    return text


def send_email():
    text = generate_email_message()
    port = settings.EMAIL_PORT
    smtp_server = settings.EMAIL_HOST
    sender_email = settings.EMAIL_HOST_USER
    password = settings.EMAIL_HOST_PASSWORD
    receiver_email = 'sarakvn@gmail.com'
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

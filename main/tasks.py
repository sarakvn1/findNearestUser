from main.generate_email import generate_email
from main.send_email import send_email

from project import celery_app

@celery_app.task()
def daily_users():
    generate_email()
    send_email()
    print("email sent successfully")

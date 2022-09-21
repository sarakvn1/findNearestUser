from dashboard.info import DashboardInfo
from dashboard.models import User
from project import celery_app


@celery_app.task()
def daily_update():
    identifiers = User.objects.all().values_list('identifier', flat=True)
    for i in list(identifiers):
        info = DashboardInfo(user_id=i)
        info.daily_update()
    print("daily update finished successfully")

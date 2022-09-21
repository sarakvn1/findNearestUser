from redis import Redis
from django.conf import settings


def redis_connector():
    DB = settings.DB_REDIS
    params = {
        'host': settings.REDIS_HOST,
        'port': settings.REDIS_PORT,
        'decode_responses': True,
        'db': DB,
    }

    if settings.REDIS_USER and settings.REDIS_PASS:
        params.update({
            'username': settings.REDIS_USER,
            'password': settings.REDIS_PASS,
        })

    client = Redis(**params)
    return client

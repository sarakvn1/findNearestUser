from django.test import TestCase

# Create your tests here.
import json

import pytest
from model_bakery import baker
from django.urls import reverse
from rest_framework.test import APIClient

from loguru import logger


@pytest.mark.django_db
def test_create_user_should_pass():
    client = APIClient()
    data = {
        "username": "sara3",
        "password": "sarakvn@gmail.com",
        "location": {"lat": 39.7622290, "lon": -86.1519750}
    }

    response = client.post('/user/', data=json.dumps(data), content_type='application/json')
    logger.info(response.content)
    assert response.status_code == 200


@pytest.mark.django_db
def test_find_nearest_user_should_pass():
    client = APIClient()
    baker.make('main.User', username='sara', location={'lat': 39.7612992, 'lon': -86.1519681})
    baker.make('main.User', username='sara1', location={'lat': 39.762241, 'lon': -86.158436})
    baker.make('main.User', username='sara2', location={'lat': 39.7622292, 'lon': -86.1578917})
    data = {"lat": 39.7622290, "lon": -86.1519750}

    response = client.post('/find-nearest', data=json.dumps(data), content_type='application/json')
    logger.info(response.content)
    assert response.status_code == 200

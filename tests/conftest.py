import pytest
import requests
import json
import settings


@pytest.fixture()
def get_token():
    data = {"email": settings.TestData.VALID_EMAIL,
            "password": settings.TestData.VALID_PASSWORD}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(settings.BASE_URL + 'users/login', data=json.dumps(data), headers=headers)
    token = response.json().get('token')
    return token

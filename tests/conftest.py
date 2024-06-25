import pytest
from assertpy import assert_that
import requests
from config import BASE_URL


@pytest.fixture
def create_token():
    headers = {'Content-Type': 'application/json'}
    payload = {"username": "admin", "password": "password123"}
    r = requests.post(f'{BASE_URL}/auth', headers=headers, json=payload)
    assert_that(r.status_code).is_equal_to(200)
    print(r, r.status_code, r.content)
    token = r.json()['token']
    return token

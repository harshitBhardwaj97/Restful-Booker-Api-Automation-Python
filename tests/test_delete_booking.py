import requests
from assertpy import assert_that
from random import randint
from config import BASE_URL
from utils.utils import generate_valid_booking_data
import pytest

@pytest.fixture(scope='module')
def booking_to_be_deleted():
    # Create a booking
    booking_data = generate_valid_booking_data()
    r = requests.post(f'{BASE_URL}/booking', json=booking_data)
    return r.json()['bookingid']

def test_delete_booking_without_token():
    random_booking_id = randint(1000, 2000)
    r = requests.delete(f'{BASE_URL}/booking/{random_booking_id}')
    print(r.content)
    assert_that("Forbidden" in r.text).is_true()
    assert_that(r.status_code).is_equal_to(403)

def test_delete_booking(booking_to_be_deleted, create_token):
    headers = {
        'Content-Type': 'application/json',
        'Cookie' : f'token={create_token}'
        }
    booking_id = booking_to_be_deleted
    r = requests.delete(f'{BASE_URL}/booking/{booking_id}', headers=headers)
    print(r.content)
    assert_that(r.status_code).is_equal_to(201)
    assert_that("Created" in r.text).is_true()
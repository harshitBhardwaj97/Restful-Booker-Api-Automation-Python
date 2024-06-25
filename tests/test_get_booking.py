import requests
from assertpy import assert_that
import pytest
from random import randint
from config import BASE_URL
from utils.utils import generate_valid_booking_data


@pytest.fixture(scope='module')
def created_booking():
    # Create a booking
    booking_data = generate_valid_booking_data()
    r = requests.post(f'{BASE_URL}/booking', json=booking_data)
    return (r.json()['bookingid'], r.json()['booking']['firstname'], r.json()['booking']['lastname'])


def test_get_booking_by_id(created_booking):
    booking_id, firstname, lastname = created_booking
    r = requests.get(f'{BASE_URL}/booking/{booking_id}')
    assert_that(r.status_code).is_equal_to(200)
    booking = r.json()
    print(booking_id, r.content)
    assert_that(booking['firstname']).is_equal_to(firstname)
    assert_that(booking['lastname']).is_equal_to(lastname)


def test_get_booking_by_not_found_id():
    not_found_id = randint(10000000, 99999999)
    print(f'Not found id is {not_found_id}')
    r = requests.get(f'{BASE_URL}/booking/{not_found_id}')
    print(r.content)
    assert_that(r.status_code).is_equal_to(404)
    assert_that("Not Found" in r.text).is_true()

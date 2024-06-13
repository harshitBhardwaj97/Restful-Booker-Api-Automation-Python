import requests
from assertpy import assert_that
import pytest
from config import BASE_URL
from utils.utils import generate_valid_booking_data

@pytest.fixture(scope='module')
def created_booking():
    # Create a booking
    booking_data = generate_valid_booking_data()
    r = requests.post(f'{BASE_URL}/booking', json=booking_data)
    r.raise_for_status()
    return r.json()['bookingid']

def test_get_bookings(created_booking):
    r = requests.get(f'{BASE_URL}/booking')
    assert_that(r.status_code).is_equal_to(200)
    ids = r.json()
    assert_that(ids).is_not_empty()
    assert_that(ids).extracting('bookingid').contains(created_booking)
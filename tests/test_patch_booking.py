import requests
from config import BASE_URL
from assertpy import assert_that
from utils.utils import *
import pytest

@pytest.fixture(scope='module')
def booking_to_be_patched():
    # Create a booking
    booking_data = generate_valid_booking_data()
    r = requests.post(f'{BASE_URL}/booking', json=booking_data)
    print(f'Initial Response body after creating a booking is \n {r.content}')
    return r.json()['bookingid']

def test_partial_update_booking(booking_to_be_patched, create_token):
    headers = {
        'Content-Type': 'application/json',
        'Cookie' : f'token={create_token}'
        }
    booking_id = booking_to_be_patched
    updated_booking_data = get_updated_data()
    r = requests.patch(f'{BASE_URL}/booking/{booking_id}', headers=headers, json=updated_booking_data)
    assert_that(r.status_code).is_equal_to(200)
    response_body = r.json()
    assert_that(response_body['firstname']).is_equal_to(updated_booking_data['firstname'])
    assert_that(response_body['lastname']).is_equal_to(updated_booking_data['lastname'])
    print(r.status_code, r.content)





import requests
from config import BASE_URL
from assertpy import assert_that
from utils.utils import *
import pytest

@pytest.fixture(scope='module')
def booking_to_be_updated():
    # Create a booking
    booking_data = generate_valid_booking_data()
    r = requests.post(f'{BASE_URL}/booking', json=booking_data)
    print(f'Initial Response body after creating a booking is \n {r.content}')
    return r.json()['bookingid']

def test_update_booking(booking_to_be_updated, create_token):
    headers = {
        'Content-Type': 'application/json',
        'Cookie' : f'token={create_token}'
        }
    booking_id = booking_to_be_updated
    updated_booking_data = generate_valid_booking_data()
    r = requests.put(f'{BASE_URL}/booking/{booking_id}', headers=headers, json=updated_booking_data)
    assert_that(r.status_code).is_equal_to(200)
    response_body = r.json()
    assert_that(response_body['firstname']).is_equal_to(updated_booking_data['firstname'])
    assert_that(response_body['lastname']).is_equal_to(updated_booking_data['lastname'])
    assert_that(response_body['totalprice']).is_equal_to(updated_booking_data['totalprice'])
    assert_that(response_body['bookingdates']['checkin']).is_equal_to(updated_booking_data['bookingdates']['checkin'])
    assert_that(response_body['bookingdates']['checkout']).is_equal_to(updated_booking_data['bookingdates']['checkout'])
    assert_that(response_body['additionalneeds']).is_equal_to(updated_booking_data['additionalneeds'])
    print(r.status_code, r.content)




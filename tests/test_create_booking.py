import requests
from config import BASE_URL
from assertpy import assert_that
from utils.utils import *

headers = {'Content-Type': 'application/json'}


def test_create_invalid_booking():
    invalid_booking_data = generate_invalid_booking_data()
    print(invalid_booking_data)
    try:
        r = requests.post(f'{BASE_URL}/booking', headers=headers, json=invalid_booking_data)
        r.raise_for_status()  # Raise exception for HTTP errors
        print(r.status_code, r.json())
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")


def test_create_valid_booking():
    valid_booking_data = generate_valid_booking_data()
    print(valid_booking_data)
    r = requests.post(f'{BASE_URL}/booking', json=valid_booking_data)
    assert_that(r.status_code).is_equal_to(200)
    response_body = r.json()
    print(f'Response is {response_body}')
    assert_that(response_body).contains('bookingid')
    assert_that(response_body['booking']['firstname']).is_equal_to(valid_booking_data['firstname'])
    print(r.status_code, r.content)

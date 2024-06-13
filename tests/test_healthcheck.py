import requests
from config import BASE_URL
from assertpy import assert_that

def test_healthcheck():
    r = requests.get(f'{BASE_URL}/ping')
    print(r, r.content)
    assert_that(r.status_code).is_equal_to(201)
    assert_that("Created" in r.text).is_true()

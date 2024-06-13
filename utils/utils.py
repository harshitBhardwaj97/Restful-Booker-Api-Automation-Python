from faker import Faker
from random import randint, choice
from datetime import timedelta

fake = Faker()

def generate_valid_booking_data():
    # Generate fake data
    firstname = fake.first_name()
    lastname = fake.last_name()
    totalprice = randint(100, 1000)
    depositpaid = choice(["true", "false"])
    checkin = fake.date_between(start_date='-1y', end_date='today')
    checkout = checkin + timedelta(days=randint(1, 30))
    additionalneeds = choice(["Breakfast", "Lunch", "Dinner", "WiFi"])

    # Format booking dates
    bookingdates = {
        "checkin": checkin.strftime('%Y-%m-%d'),
        "checkout": checkout.strftime('%Y-%m-%d')
    }

    # Construct the booking data dictionary
    booking_data = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": bookingdates,
        "additionalneeds": additionalneeds
    }

    return booking_data

def generate_invalid_booking_data():
    # Generate fake data
    firstname = fake.first_name()
    lastname = fake.last_name()
    totalprice = randint(100, 1000)
    depositpaid = fake.name_nonbinary()
    additionalneeds = choice(["Breakfast", "Lunch", "Dinner", "WiFi"])

    # Construct the booking data dictionary
    invalid_booking_data = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": [],
        "additionalneeds": additionalneeds
    }

    return invalid_booking_data

def get_updated_data():
    firstname = fake.first_name()
    lastname = fake.last_name()
    updated_data = {
        "firstname": firstname,
        "lastname": lastname
    }
    return updated_data

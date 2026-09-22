import pytest
import requests

BASE_URL = "https://restful-booker.herokuapp.com"

#fixture for auth token
@pytest.fixture(scope="session")  # means this runs once for the whole test run, not once per test
def auth_token():
    payload={
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(f"{BASE_URL}/auth", json=payload)
    assert response.status_code == 200
    return response.json()["token"]

#fixture that creates a booking
@pytest.fixture()
def created_booking():
    payload = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2025-01-01", "checkout": "2025-01-05"},
        "additionalneeds": "Breakfast"
    }
    response = requests.post(f"{BASE_URL}/booking", json=payload)
    assert response.status_code == 200
    return response.json()  # contains bookingid + booking details
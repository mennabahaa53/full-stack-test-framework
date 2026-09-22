import requests
import conftest  


BASE_URL = "https://restful-booker.herokuapp.com"

def test_create_booking(created_booking):
    assert "bookingid" in created_booking
    assert created_booking["booking"]["firstname"] == "John"

def test_get_booking_by_id(created_booking):
    booking_id = created_booking["bookingid"]
    response = requests.get(f"{BASE_URL}/booking/{booking_id}")
    assert response.status_code == 200
    assert response.json()["firstname"] == "John"

def test_update_booking_requires_auth(created_booking, auth_token):
    booking_id = created_booking["bookingid"]
    response = requests.put(
        f"{BASE_URL}/booking/{booking_id}",
        json={
            "firstname": "Jane",
            "lastname": "Doe",
            "totalprice": 200,
            "depositpaid": True,
            "bookingdates": {"checkin": "2025-02-01", "checkout": "2025-02-05"}
        },
        headers={"Cookie": f"token={auth_token}"}
    )
    assert response.status_code == 200
    assert response.json()["firstname"] == "Jane"

def test_update_booking_without_auth_fails(created_booking):
    booking_id = created_booking["bookingid"]
    response = requests.put(
        f"{BASE_URL}/booking/{booking_id}",
        json={"firstname": "Hacker"}
    )
    assert response.status_code in (403, 401)  # should be rejected

def test_delete_booking_requires_auth(created_booking, auth_token):
    booking_id = created_booking["bookingid"]
    response = requests.delete(
        f"{BASE_URL}/booking/{booking_id}",
        headers={"Cookie": f"token={auth_token}"}
    )
    assert response.status_code == 201  # restful-booker returns 201 on delete

def test_missing_required_fields_in_booking():
    incomplete_payload = {
        "firstname": "John"
        # missing: lastname, totalprice, depositpaid, bookingdates
    }
    response = requests.post(f"{BASE_URL}/booking",json=incomplete_payload)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 500

def test_delete_booking_without_auth(created_booking):
    booking_id = created_booking["bookingid"]

    response = requests.delete(
        f"{BASE_URL}/booking/{booking_id}"
    )
    assert response.status_code == 403
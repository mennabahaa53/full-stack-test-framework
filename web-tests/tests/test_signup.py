from pages.signup_page import SignupPage
import random

def test_full_signup(driver):
    driver.get("https://automationexercise.com/login")

    random_number = random.randint(1, 1000000)
    unique_email = f"testuser{random_number}@example.com"

    signup_page = SignupPage(driver)
    signup_page.start_signup("Test User", unique_email)
    signup_page.complete_account_details(
        password="TestPassword123",
        day="23",
        month="September",
        year="2019",
        first_name="Test",
        last_name="User",
        address="123 Test Street",
        country="United States",
        state="Test State",
        city="Test City",
        zipcode="12345",
        mobile="1234567890"
    )

    assert "account_created" in driver.current_url.lower()
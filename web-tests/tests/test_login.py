from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_click_signup_login_link(driver):
    driver.get("https://automationexercise.com")

    signup_login_link = driver.find_element(By.LINK_TEXT, "Signup / Login")
    signup_login_link.click()

    assert "login" in driver.current_url


def test_login_with_invalid_credentials(driver):
    driver.get("https://automationexercise.com/login")

    login_page = LoginPage(driver)
    login_page.login("fake_user@example.com", "wrongpassword")

    wait = WebDriverWait(driver, 10)
    wait.until(lambda d: "incorrect" in d.page_source.lower())

    assert "incorrect" in driver.page_source.lower()

def test_login_with_valid_credentials(driver):
    driver.get("https://automationexercise.com/login")

    login_page = LoginPage(driver)
    login_page.login("mennabahaa.qa.test@example.com", "TestPassword123")

    wait = WebDriverWait(driver, 10)
    wait.until(lambda d: "logged in as" in d.page_source.lower())

    assert "logged in as" in driver.page_source.lower()
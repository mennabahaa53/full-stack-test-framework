from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

def test_click_signup_login_link():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")

    signup_login_link = driver.find_element(By.LINK_TEXT, "Signup / Login")
    signup_login_link.click()

    assert "login" in driver.current_url
    driver.quit()

def test_login_with_invalid_credentials():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com/login")

    login_page = LoginPage(driver)
    login_page.login("fake_user@example.com", "wrongpassword")

    assert "incorrect" in driver.page_source.lower()
    driver.quit()

def test_login_with_valid_credentials():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com/login")

    login_page = LoginPage(driver)
    login_page.login("mennabahaa.qa.test@example.com", "TestPassword123")

    assert "logged in as" in driver.page_source.lower()
    driver.quit()
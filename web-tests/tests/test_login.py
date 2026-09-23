from selenium import webdriver
from selenium.webdriver.common.by import By

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
    
    email_field = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-email']")
    password_field = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']")
    
    email_field.send_keys("fake_user@example.com")
    password_field.send_keys("wrongpassword")
    
    login_button = driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']")
    login_button.click()
    
    assert "incorrect" in driver.page_source.lower()
    driver.quit()
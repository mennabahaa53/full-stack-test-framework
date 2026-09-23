from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random

def test_signup_step_one():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com/login")

    random_number = random.randint(1, 1000000)
    unique_email = f"mennabahaa.qa.test{random_number}@example.com"

    #first page
    name_field = driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-name']")
    name_field.send_keys("Test QA")
    email_field = driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']")
    email_field.send_keys(unique_email)

    signup_button_step1 = driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']")
    signup_button_step1.click()

    #second page-part1
    title_field_mr = driver.find_element(By.CSS_SELECTOR, "input#id_gender1")
    title_field_mr.click()

    password_field = driver.find_element(By.CSS_SELECTOR, "input[data-qa='password']")
    password_field.send_keys("TestPassword123")

    #second page-part2
    day_dropdown = driver.find_element(By.CSS_SELECTOR, "select[data-qa='days']")
    Select(day_dropdown).select_by_visible_text("23")

    month_dropdown = driver.find_element(By.CSS_SELECTOR, "select[data-qa='months']")
    Select(month_dropdown).select_by_visible_text("September")

    year_dropdown = driver.find_element(By.CSS_SELECTOR, "select[data-qa='years']")
    Select(year_dropdown).select_by_visible_text("2019")

    newsletter_checkbox = driver.find_element(By.ID, "newsletter")
    newsletter_checkbox.click()

    offers_checkbox = driver.find_element(By.ID, "optin")
    offers_checkbox.click()

    #second page-part3
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='first_name']").send_keys("Test")
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='last_name']").send_keys("User")
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='company']").send_keys("Test Company")
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='address']").send_keys("123 Test Street")
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='address2']").send_keys("Suite 456")

    country_dropdown = driver.find_element(By.CSS_SELECTOR, "select[data-qa='country']")
    Select(country_dropdown).select_by_visible_text("United States")

    driver.find_element(By.CSS_SELECTOR, "input[data-qa='state']").send_keys("Test State")
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='city']").send_keys("Test City")
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='zipcode']").send_keys("12345")
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='mobile_number']").send_keys("1234567890")

    signup_button_final = driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']")
    signup_button_final.click()

    assert "account_created" in driver.current_url.lower()
    driver.quit()
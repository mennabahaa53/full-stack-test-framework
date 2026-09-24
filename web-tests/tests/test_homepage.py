from selenium import webdriver

def test_homepage_loads(driver):
    driver.get("https://automationexercise.com")
    assert "Automation Exercise" in driver.title
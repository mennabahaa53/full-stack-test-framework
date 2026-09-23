from selenium import webdriver

def test_homepage_loads():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    print(driver.title)
    driver.quit()
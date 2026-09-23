from selenium import webdriver

def test_homepage_loads():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    #print(driver.title)
    assert "Automation Exercise" in driver.title
    driver.quit()
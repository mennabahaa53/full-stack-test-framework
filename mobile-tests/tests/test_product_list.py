from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import os
import time

def test_tap_first_product():
    apk_path = os.path.abspath("mobile-tests/app/mda-2.3.0-27.apk")

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"
    options.app = apk_path

    

    from selenium.webdriver.common.by import By

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    time.sleep(3)

    try:
        ok_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("OK")')
        ok_button.click()
    except:
        pass


    first_product = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Sauce Labs Backpack")'
    )

    first_product = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Sauce Labs Backpack")'
    )
    first_product.click()

    assert driver.current_activity is not None

    driver.quit()
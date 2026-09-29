from appium import webdriver
from appium.options.android import UiAutomator2Options
import os

def test_app_launches():
    apk_path = os.path.abspath("mobile-tests/app/mda-2.3.0-27.apk")

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"
    options.app = apk_path

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    assert driver.current_activity is not None

    driver.quit()
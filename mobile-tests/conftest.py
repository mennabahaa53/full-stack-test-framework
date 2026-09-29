import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import os
import time

@pytest.fixture()
def driver():
    apk_path = os.path.abspath("app/mda-2.3.0-27.apk")

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"
    options.app = apk_path

    appium_driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    time.sleep(3)

    yield appium_driver

    appium_driver.quit()
    time.sleep(2)
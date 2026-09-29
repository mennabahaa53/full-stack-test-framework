from appium import webdriver
from appium.options.android import UiAutomator2Options
from pages.products_page import ProductsPage
import os
import time

def test_tap_first_product():
    apk_path = os.path.abspath("app/mda-2.3.0-27.apk")

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"
    options.app = apk_path

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    time.sleep(3)

    products_page = ProductsPage(driver)
    products_page.dismiss_compatibility_dialog()
    products_page.tap_product_by_name("Sauce Labs Backpack")

    assert driver.current_activity is not None

    driver.quit()
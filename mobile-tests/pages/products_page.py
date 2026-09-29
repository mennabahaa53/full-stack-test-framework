from appium.webdriver.common.appiumby import AppiumBy

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def dismiss_compatibility_dialog(self):
        try:
            ok_button = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("OK")')
            ok_button.click()
        except:
            pass

    def tap_product_by_name(self, product_name):
        product = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{product_name}")'
        )
        product.click()
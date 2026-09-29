from pages.products_page import ProductsPage

def test_tap_first_product(driver):
    products_page = ProductsPage(driver)
    products_page.dismiss_compatibility_dialog()
    products_page.tap_product_by_name("Sauce Labs Backpack")

    assert driver.current_activity is not None

def test_view_product_details(driver):
    products_page = ProductsPage(driver)
    products_page.dismiss_compatibility_dialog()
    products_page.tap_product_by_name("Sauce Labs Backpack")

    import time
    time.sleep(2)

    assert "Sauce Labs Backpack" in driver.page_source
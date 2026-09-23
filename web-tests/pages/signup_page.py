
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class SignupPage:
    def __init__(self, driver):
        self.driver = driver

    NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")

    TITLE_MR = (By.CSS_SELECTOR, "input#id_gender1")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-qa='password']")
    DAY_DROPDOWN = (By.CSS_SELECTOR, "select[data-qa='days']")
    MONTH_DROPDOWN = (By.CSS_SELECTOR, "select[data-qa='months']")
    YEAR_DROPDOWN = (By.CSS_SELECTOR, "select[data-qa='years']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='first_name']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='last_name']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "input[data-qa='address']")
    COUNTRY_DROPDOWN = (By.CSS_SELECTOR, "select[data-qa='country']")
    STATE_INPUT = (By.CSS_SELECTOR, "input[data-qa='state']")
    CITY_INPUT = (By.CSS_SELECTOR, "input[data-qa='city']")
    ZIPCODE_INPUT = (By.CSS_SELECTOR, "input[data-qa='zipcode']")
    MOBILE_INPUT = (By.CSS_SELECTOR, "input[data-qa='mobile_number']")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-qa='create-account']")

    def start_signup(self, name, email):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.SIGNUP_BUTTON).click()

    def complete_account_details(self, password, day, month, year, first_name, last_name,
                                   address, country, state, city, zipcode, mobile):
        self.driver.find_element(*self.TITLE_MR).click()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

        Select(self.driver.find_element(*self.DAY_DROPDOWN)).select_by_visible_text(day)
        Select(self.driver.find_element(*self.MONTH_DROPDOWN)).select_by_visible_text(month)
        Select(self.driver.find_element(*self.YEAR_DROPDOWN)).select_by_visible_text(year)

        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)

        Select(self.driver.find_element(*self.COUNTRY_DROPDOWN)).select_by_visible_text(country)

        self.driver.find_element(*self.STATE_INPUT).send_keys(state)
        self.driver.find_element(*self.CITY_INPUT).send_keys(city)
        self.driver.find_element(*self.ZIPCODE_INPUT).send_keys(zipcode)
        self.driver.find_element(*self.MOBILE_INPUT).send_keys(mobile)

        create_account_btn = self.driver.find_element(*self.CREATE_ACCOUNT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", create_account_btn)
        create_account_btn.click()
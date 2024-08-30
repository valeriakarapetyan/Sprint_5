from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.locators import StellarBurgersLocators
from src.config import Config


class TestLogOut:
    def test_logout_from_account(self, driver, registration):
        creds = registration
        driver.get(Config.URL)
        driver.find_element(*StellarBurgersLocators.LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_ON_LOGIN_FORM).send_keys(creds["email"])
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_ON_LOGIN_FORM).send_keys(creds["pass"])

        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_ON_LOGIN_FORM).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.PLACE_AN_ORDER_BUTTON))

        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGOUT_BUTTON_ON_ACCOUNT_PAGE))

        driver.find_element(*StellarBurgersLocators.LOGOUT_BUTTON_ON_ACCOUNT_PAGE).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.PASSWORD_RECOVERY_BUTTON))

        assert f'{Config.URL}/login' == driver.current_url

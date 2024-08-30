from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.locators import StellarBurgersLocators
from src.config import Config


class TestTransitionFromAccountToConstructor:

    def test_successful_transition_by_constructor_button(self, driver, login):
        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGOUT_BUTTON_ON_ACCOUNT_PAGE))
        driver.find_element(*StellarBurgersLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.PLACE_AN_ORDER_BUTTON))
        assert f'{Config.URL}/' == driver.current_url

    def test_successful_transition_by_logo(self, driver, login):
        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGOUT_BUTTON_ON_ACCOUNT_PAGE))
        driver.find_element(*StellarBurgersLocators.STELLAR_BURGERS_LABEL).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.PLACE_AN_ORDER_BUTTON))
        assert f'{Config.URL}/' == driver.current_url

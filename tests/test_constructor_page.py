from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.locators import StellarBurgersLocators
from src.config import Config


class TestTransitionsFromConstructorPage:

    def test_transition_to_sauces(self, driver):
        driver.get(Config.URL)
        WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.LOGIN_ACCOUNT_BUTTON))
        driver.find_element(*StellarBurgersLocators.SAUCES_BUTTON).click()
        new_class = driver.find_element(*StellarBurgersLocators.SAUCES_BUTTON).get_attribute("class")
        assert 'tab_tab_type_current__2BEPc' in new_class

    def test_transition_to_fillings(self, driver):
        driver.get(Config.URL)
        WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.LOGIN_ACCOUNT_BUTTON))
        driver.find_element(*StellarBurgersLocators.FILLINGS_BUTTON).click()
        new_class = driver.find_element(*StellarBurgersLocators.FILLINGS_BUTTON).get_attribute("class")
        assert 'tab_tab_type_current__2BEPc' in new_class

    def test_transition_to_buns(self, driver):
        driver.get(Config.URL)
        WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.LOGIN_ACCOUNT_BUTTON))
        driver.find_element(*StellarBurgersLocators.FILLINGS_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.BUNS_BUTTON).click()
        new_class = driver.find_element(*StellarBurgersLocators.BUNS_BUTTON).get_attribute("class")
        assert 'tab_tab_type_current__2BEPc' in new_class

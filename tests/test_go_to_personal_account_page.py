from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.locators import StellarBurgersLocators
from src.config import Config


class TestStellarBurgersPersonalAccount:

    def test_successful_transition_to_personal_account_page(self, driver, login):
        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGOUT_BUTTON_ON_ACCOUNT_PAGE))
        assert f'{Config.URL}/account/profile' == driver.current_url

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.locators import StellarBurgersLocators
from src.config import Config


class TestStellarBurgersLogin:

    # вход по кнопке «Войти в аккаунт» на главной
    def test_login_by_enter_account_button(self, driver, login):
        assert f'{Config.URL}/' == driver.current_url and \
               driver.find_element(*StellarBurgersLocators.PLACE_AN_ORDER_BUTTON).text == "Оформить заказ"

    # вход через кнопку «Личный кабинет»
    def test_login_by_personal_account_button(self, driver, registration):
        creds = registration
        driver.get(Config.URL)
        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_ON_LOGIN_FORM).send_keys(creds["email"])
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_ON_LOGIN_FORM).send_keys(creds["pass"])

        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_ON_LOGIN_FORM).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.PLACE_AN_ORDER_BUTTON))

        assert f'{Config.URL}/' == driver.current_url and \
               driver.find_element(*StellarBurgersLocators.PLACE_AN_ORDER_BUTTON).text == "Оформить заказ"

    # вход через кнопку в форме регистрации
    def test_login_by_login_button_on_registration_form(self, driver, registration):
        creds = registration
        driver.get(f'{Config.URL}/register')
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_ON_REGISTRATION_FORM).click()
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_ON_LOGIN_FORM).send_keys(creds["email"])
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_ON_LOGIN_FORM).send_keys(creds["pass"])

        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_ON_LOGIN_FORM).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.PLACE_AN_ORDER_BUTTON))

        assert f'{Config.URL}/' == driver.current_url and \
               driver.find_element(*StellarBurgersLocators.PLACE_AN_ORDER_BUTTON).text == "Оформить заказ"

    # вход через кнопку в форме восстановления пароля
    def test_login_by_login_button_on_password_recovery_form(self, driver, registration):
        creds = registration
        driver.find_element(*StellarBurgersLocators.PASSWORD_RECOVERY_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_ON_RECOVERY_FORM).click()

        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_ON_LOGIN_FORM).send_keys(creds["email"])
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_ON_LOGIN_FORM).send_keys(creds["pass"])

        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_ON_LOGIN_FORM).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.PLACE_AN_ORDER_BUTTON))

        assert f'{Config.URL}/' == driver.current_url and \
               driver.find_element(*StellarBurgersLocators.PLACE_AN_ORDER_BUTTON).text == "Оформить заказ"

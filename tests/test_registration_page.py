import random
from src.locators import StellarBurgersLocators
from src.config import Config
from src.helpers import generate_email


class TestStellarBurgersRegistration:

    def test_successful_sign_up(self, driver, registration):
        assert f'{Config.URL}/login' == driver.current_url

    # здесь не использую фикстуру registration, т.к. нужен короткий пароль
    def test_short_password_shows_error(self, driver):
        random_email = generate_email()

        driver.get(f'{Config.URL}/register')

        driver.find_element(*StellarBurgersLocators.NAME_FIELD_ON_REGISTRATION_FORM).send_keys("Валерия")
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_ON_REGISTRATION_FORM).send_keys(random_email)

        random_short_pass = random.randint(10000, 99999)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_ON_REGISTRATION_FORM).send_keys(random_short_pass)

        driver.find_element(*StellarBurgersLocators.SIGNUP_BUTTON_ON_REGISTRATION_FORM).click()

        assert driver.find_element(*StellarBurgersLocators.INCORRECT_PASS_ON_REGISTRATION_FORM).text == "Некорректный пароль"

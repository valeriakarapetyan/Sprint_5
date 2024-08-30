import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from src.config import Config
from src.locators import StellarBurgersLocators
from src.helpers import generate_password, generate_email


def browser_settings():
    chrome_options = webdriver.ChromeOptions()
    return chrome_options


@pytest.fixture
def driver():
    chrome = webdriver.Chrome(options=browser_settings())
    chrome.get(Config.URL)
    yield chrome
    chrome.quit()


@pytest.fixture
def registration(driver):
    random_email = generate_email()
    random_pass = generate_password()
    driver.get(Config.URL)

    WebDriverWait(driver, 15).until(
        expected_conditions.element_to_be_clickable(StellarBurgersLocators.LOGIN_ACCOUNT_BUTTON))
    driver.find_element(*StellarBurgersLocators.LOGIN_ACCOUNT_BUTTON).click()

    driver.find_element(*StellarBurgersLocators.SIGNUP_ACCOUNT_BUTTON_ON_LOGIN_FORM).click()

    driver.find_element(*StellarBurgersLocators.NAME_FIELD_ON_REGISTRATION_FORM).send_keys("Валерия")
    driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_ON_REGISTRATION_FORM).send_keys(random_email)
    driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_ON_REGISTRATION_FORM).send_keys(random_pass)

    driver.find_element(*StellarBurgersLocators.SIGNUP_BUTTON_ON_REGISTRATION_FORM).click()

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_BUTTON_ON_LOGIN_FORM))

    creds = {
        "email": random_email,
        "pass": random_pass
    }

    yield creds


@pytest.fixture
def login(driver, registration):
    creds = registration
    driver.get(Config.URL)
    driver.find_element(*StellarBurgersLocators.LOGIN_ACCOUNT_BUTTON).click()
    driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_ON_LOGIN_FORM).send_keys(creds["email"])
    driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_ON_LOGIN_FORM).send_keys(creds["pass"])

    driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_ON_LOGIN_FORM).click()

    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(StellarBurgersLocators.PLACE_AN_ORDER_BUTTON))

import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators
from constants import BASE_URL

class TestRegistration:
    def test_registration_valid_data_shows_username(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.visibility_of_element_located(locators.HEADER_AUTH_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(locators.NO_ACCOUNT_BUTTON)).click()

        unique_email = f"auto_test_{int(time.time())}@test.ru"

        wait.until(EC.visibility_of_element_located(locators.REG_EMAIL_FIELD)).send_keys(unique_email)
        wait.until(EC.visibility_of_element_located(locators.REG_PASSWORD_FIELD)).send_keys("Qwerty123!")
        wait.until(EC.visibility_of_element_located(locators.REG_REPEAT_PASSWORD_FIELD)).send_keys("Qwerty123!")
        wait.until(EC.visibility_of_element_located(locators.CREATE_ACCOUNT_BUTTON)).click()

        username_element = wait.until(EC.visibility_of_element_located(locators.MAIN_PAGE_USERNAME))
        assert "User" in username_element.text

    def test_registration_invalid_email_shows_error_message(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.visibility_of_element_located(locators.HEADER_AUTH_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(locators.NO_ACCOUNT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(locators.REG_EMAIL_FIELD)).send_keys("invalid_email")
        wait.until(EC.visibility_of_element_located(locators.REG_PASSWORD_FIELD)).send_keys("Qwerty123!")
        wait.until(EC.visibility_of_element_located(locators.REG_REPEAT_PASSWORD_FIELD)).send_keys("Qwerty123!")
        wait.until(EC.visibility_of_element_located(locators.CREATE_ACCOUNT_BUTTON)).click()

        assert "Ошибка" in wait.until(
            EC.visibility_of_element_located(locators.REG_EMAIL_ERROR_MESSAGE)
        ).text

    def test_registration_existing_user_shows_error_message(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.visibility_of_element_located(locators.HEADER_AUTH_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(locators.NO_ACCOUNT_BUTTON)).click()

        unique_email = f"existing_user_{int(time.time())}@qa.ru"

        wait.until(EC.visibility_of_element_located(locators.REG_EMAIL_FIELD)).send_keys(unique_email)
        wait.until(EC.visibility_of_element_located(locators.REG_PASSWORD_FIELD)).send_keys("Qwerty123!")
        wait.until(EC.visibility_of_element_located(locators.REG_REPEAT_PASSWORD_FIELD)).send_keys("Qwerty123!")
        wait.until(EC.visibility_of_element_located(locators.CREATE_ACCOUNT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(locators.MAIN_PAGE_USERNAME))

        wait.until(EC.visibility_of_element_located(locators.LOGOUT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(locators.HEADER_AUTH_BUTTON))

        wait.until(EC.visibility_of_element_located(locators.HEADER_AUTH_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(locators.NO_ACCOUNT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(locators.REG_EMAIL_FIELD))

        wait.until(EC.visibility_of_element_located(locators.REG_EMAIL_FIELD)).send_keys(unique_email)
        wait.until(EC.visibility_of_element_located(locators.REG_PASSWORD_FIELD)).send_keys("Qwerty123!")
        wait.until(EC.visibility_of_element_located(locators.REG_REPEAT_PASSWORD_FIELD)).send_keys("Qwerty123!")
        wait.until(EC.visibility_of_element_located(locators.CREATE_ACCOUNT_BUTTON)).click()

        assert "Ошибка" in wait.until(
            EC.visibility_of_element_located(locators.REG_EMAIL_ERROR_MESSAGE)
        ).text
        
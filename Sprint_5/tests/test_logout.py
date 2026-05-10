import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators

class TestLogout:
    def test_logout_shows_auth_button(self, driver):
        driver.get("https://qa-desk.education-services.ru/")
        wait = WebDriverWait(driver, 10)

        wait.until(EC.visibility_of_element_located(locators.HEADER_AUTH_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(locators.NO_ACCOUNT_BUTTON)).click()

        unique_email = f"logout_test_{int(time.time())}@qa.ru"

        wait.until(EC.visibility_of_element_located(locators.REG_EMAIL_FIELD)).send_keys(unique_email)
        wait.until(EC.visibility_of_element_located(locators.REG_PASSWORD_FIELD)).send_keys("Qwerty123!")
        wait.until(EC.visibility_of_element_located(locators.REG_REPEAT_PASSWORD_FIELD)).send_keys("Qwerty123!")
        wait.until(EC.visibility_of_element_located(locators.CREATE_ACCOUNT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(locators.MAIN_PAGE_USERNAME))
        wait.until(EC.visibility_of_element_located(locators.LOGOUT_BUTTON)).click()

        # Ждём, пока кнопка входа снова станет видимой
        auth_button = wait.until(EC.visibility_of_element_located(locators.HEADER_AUTH_BUTTON))
        assert auth_button.is_displayed()
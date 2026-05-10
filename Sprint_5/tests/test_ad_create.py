# tests/test_ad_create.py
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators


class TestAdCreateUnauthorized:
    def test_create_ad_unauthorized_shows_auth_modal(self, driver):
        driver.get("https://qa-desk.education-services.ru/")
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(locators.CREATE_AD_BUTTON)).click()

        modal_title = wait.until(
            EC.visibility_of_element_located(locators.AUTH_MODAL_TITLE)
        )
        assert modal_title.text == "Чтобы разместить объявление, авторизуйтесь"


class TestAdCreateAuthorized:
    def test_create_ad_authorized_shows_in_profile(self, driver):
        driver.get("https://qa-desk.education-services.ru/")
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(locators.HEADER_AUTH_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(locators.NO_ACCOUNT_BUTTON)).click()

        unique_email = f"ad_test_{int(time.time())}@qa.ru"
        password = "Qwerty123!"

        wait.until(EC.visibility_of_element_located(locators.REG_EMAIL_FIELD)).send_keys(unique_email)
        wait.until(EC.visibility_of_element_located(locators.REG_PASSWORD_FIELD)).send_keys(password)
        wait.until(EC.visibility_of_element_located(locators.REG_REPEAT_PASSWORD_FIELD)).send_keys(password)
        wait.until(EC.element_to_be_clickable(locators.CREATE_ACCOUNT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(locators.MAIN_PAGE_USERNAME))

        wait.until(EC.element_to_be_clickable(locators.CREATE_AD_BUTTON)).click()
        
        # wait.until(EC.element_to_be_clickable(locators.AD_PUBLISH_BUTTON))

        unique_title = f"Тестовый товар {int(time.time())}"
        wait.until(EC.visibility_of_element_located(locators.AD_NAME_FIELD2)).send_keys(unique_title)

        unique_description = f"Тестовый товар {int(time.time())}"
        wait.until(EC.visibility_of_element_located(locators.AD_DESCRIPTION_FIELD)).send_keys(unique_description)
        
        wait.until(EC.visibility_of_element_located(locators.AD_PRICE_FIELD)).send_keys("1500")

        driver.find_element(*locators.AD_CATEGORY_DROPDOWN).click()
        driver.find_element(*locators.AD_CATEGORY_OPTION).click()

        driver.find_element(*locators.AD_CITY_DROPDOWN).click()
        driver.find_element(*locators.AD_CITY_OPTION).click()

        driver.find_element(*locators.AD_CONDITION_USED_RADIO).click()

        old_publish_btn = driver.find_element(*locators.AD_PUBLISH_BUTTON)
        old_publish_btn.click()

        WebDriverWait(driver, 10).until(EC.staleness_of(old_publish_btn))

        driver.find_element(*locators.HEADER_AVATAR_BUTTON).click()

        wait.until(EC.presence_of_element_located(locators.AD_CARD))

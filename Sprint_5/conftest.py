import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    """Запускает браузер перед тестом и закрывает после"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
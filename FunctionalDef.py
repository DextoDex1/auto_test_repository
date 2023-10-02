import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from modelmy import LocatorVariable

@pytest.fixture
def progon_bank(driver):
    driver.get(LocatorVariable.NAVIGATE)
    driver.find_element(LocatorVariable.LOGIN_BUTTON).click()
    driver.find_element(LocatorVariable.APPROVE).click()
    crypto = driver.find_element(LocatorVariable.HELLO_WORLD)
    return crypto
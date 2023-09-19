import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from modelmy import LocatorVariable

@pytest.fixture
def ProgonBank(driver):
    driver.get(LocatorVariable.navigate)
    driver.find_element(By.ID, LocatorVariable.Login_button).click()
    driver.find_element(By.ID, LocatorVariable.Approve).click()
    crypto = driver.find_element(By.ID, LocatorVariable.HelloWorld)
    return crypto
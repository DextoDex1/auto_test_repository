import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from modelmy import LocatorVariable


@pytest.mark.parametrize(
    'result, test',
    [
        (1, 'check'), #Должна быть ошибка
        ('Hello World!', 'Hello World!') #Тест должен пройти
    ]
)
def test_one_login(driver, result, test):

    driver.get(LocatorVariable.navigate)
    driver.find_element(By.ID, LocatorVariable.Login_button).click()
    driver.find_element(By.ID, LocatorVariable.Approve).click()
    crypto = driver.find_element(By.ID, LocatorVariable.HelloWorld)
    assert str(result) in crypto.text
    assert str(test) in crypto.text
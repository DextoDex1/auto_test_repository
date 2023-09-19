import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from modelmy import LocatorVariable
from FunctionalDef import ProgonBank


@pytest.mark.parametrize(
    'result, test',
    [
        (1, 'check'),                    #Должна быть ошибка
        ('Hello World!', 'Hello World!') #Тест должен пройти
    ]
)
def test_one_login(result, test, ProgonBank):
    assert str(result) in ProgonBank.text
    assert str(test) in ProgonBank.text
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--window-size=1980,1080')
chrome_options.add_argument('--disable-application-cache')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--ignore-certificate-errors')
try:
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
except Exception:
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager(driver_version="114.0.5735.90").install()),
        options=chrome_options
    )


def test_one_login():
    driver.get('https://idemo.bspb.ru/')
    driver.find_element(By.ID, 'login-button').click()
    driver.find_element(By.ID, 'login-otp-button').click()
    result = driver.find_element(By.ID, 'user-greeting')
    assert 'Hello World!' in result.text


def test_two_login():
    driver.get('https://idemo.bspb.ru/')
    driver.find_element(By.ID, 'login-button').click()
    driver.find_element(By.ID, 'login-otp-button').click()
    result1 = driver.find_element(By.ID, 'suggest-form-title')
    assert '"Умный" перевод' in result1.text

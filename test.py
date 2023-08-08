from selenium import webdriver
import pytest
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--window-size=1980,1080')
chrome_options.add_argument('--disable-application-cache')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(chrome_options)

driver.get('https://idemo.bspb.ru/')
driver.find_element(By.ID, 'login-button').click()
driver.find_element(By.ID, 'login-otp-button').click()
result = driver.find_element(By.ID, 'bank-overview')


assert 'bank-overview' in result.text

try:
    driver.find_element(By.ID, 'bank-overview')
    print('Success Login')
except:
    print('You Not Login Bank')
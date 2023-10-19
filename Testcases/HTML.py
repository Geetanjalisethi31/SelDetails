from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# instance of Options class allows
# us to configure Headless Chrome
options = Options()
# initializing webdriver for Chrome with our options
driver = webdriver.Chrome(options=options)

driver.get('https://www.google.co.in')
driver.maximize_window()
driver.implicitly_wait(20)
time.sleep(10)
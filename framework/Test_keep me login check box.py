from  unittest import TestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
class test_Acti_time(TestCase):
    def test_Keep_me_login(self):
        options=Options()
        driver=webdriver.Firefox(options=options)
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get('https://demo.actitime.com/login.do')
        checkbx = driver.find_element(By.XPATH, '//input[@type="checkbox"]')
        status=checkbx.is_selected()
        assert status== True
        driver.quit()

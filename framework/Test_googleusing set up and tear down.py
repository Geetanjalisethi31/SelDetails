#TC-1Verify TItle of page
#TC-2 : Verify Gmail link is enabled
#TC-3: Search python


from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
class test_Google(TestCase):
        def setUp(self):
            self.options = Options()
            self.driver = webdriver.Firefox(options=self.options)
            self.driver.maximize_window()
            self.driver.get('https://www.google.com/')


        def tearDown(self):
            self.driver.quit()

        def test_Title(self):


            titl = self.driver.title
            assert titl == 'Google', 'title not match'
            # driver.quit()


        def test_Gmail(self):
            '''options = Options()
            driver = webdriver.Firefox(options=options)
            driver.maximize_window()
            driver.get('https://www.google.com/')'''



            ele = self.driver.find_element(By.LINK_TEXT, 'Gmail')

            status = ele.is_enabled()

        def test_search(self):
            '''options = Options()
            driver = webdriver.Firefox(options=options)
            driver.maximize_window()
            driver.get('https://www.google.com/')'''



            findEle = self.driver.find_element(By.NAME, 'q')
            findEle.send_keys('python')
            content = findEle.get_attribute('value')
            time.sleep(10)
            assert content == 'python', 'content not displayed'




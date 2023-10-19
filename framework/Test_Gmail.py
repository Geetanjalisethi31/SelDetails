from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
class test_Gmail(TestCase):
    def test_gmail_title(self):
        options = Options()
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
        driver.get('https://www.google.com/')
        driver.find_element(By.LINK_TEXT, 'Gmail').click()
        driver.implicitly_wait(10)
        act_title = driver.title
        exp_title='Gmail: Private and secure email at no cost | Google Workspace'
        assert act_title==exp_title,'not match'
        '''if titl=='Gmail: Private and  email at no cost | Google Workspace':
            print('Test case Passed')
        else:
            print('Test Case failed')'''

        driver.quit()




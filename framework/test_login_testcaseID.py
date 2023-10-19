from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


from framework.login_Actimize_webpage import login


class TestLoginValid(TestCase):
    def setUp(self):

        self.options=Options()
        self.driver=webdriver.Firefox(options=self.options)
        #self.driver.maximize_window()
        #self.driver.implicitly_wait(20)
        self.driver.get('https://demo.actitime.com/login.do')
        self.login_webpage=login(self.driver)

    def tearDown(self):
        self.driver.quit()

    #Testcase steps:
    def test_username_textbox(self):
        #step-1:go to log in page
        self.login_webpage.wait_for_login_page_to_load()
        #step-2:enter use name & check content is displayed
        self.login_webpage.get_Username_textBox().send_keys('admin')

        content=self.login_webpage.get_Username_textBox().get_attribute('value')
        assert content=='admin'
        #3-verify place holder
        placeholder=self.login_webpage.get_Username_textBox().get_attribute('placeholder')
        assert placeholder=='Username'
        #4-verify username is not masked
        visibility=self.login_webpage.get_Username_textBox().get_attribute('type')
        assert visibility!='password'

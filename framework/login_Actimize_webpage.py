from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class login(TestCase):
    def __init__(self,driver):
        self.driver=driver


    def get_Username_textBox(self):
        try:
            #un=

            return self.driver.find_element(By.ID, 'username')
        except:
            return None

    def get_Password_textBox(self):
        try:
            return self.driver.find_element(By.NAME, 'pwd')
        except:
            return None
    def get_login_Button(self):
        try:
            return self.driver.find_element(By.ID,'loginButton')
        except:
            return None
    def get_Next_button(self):
        try:
            return self.driver.find_element(By.LINK_TEXT,'Next')
        except:
            return None
    def wait_for_login_page_to_load(self):
        wait=WebDriverWait(timeout=30,driver=self.driver)
        #wait.until(expected_conditions.visibility_of(self.get_Username_textBox()))
        wait.until(expected_conditions.visibility_of(self.get_Password_textBox()))
        wait.until(expected_conditions.visibility_of(self.get_login_Button()))




'''print('*************explicitly wait************')
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from  selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
options=Options()
driver=webdriver.Firefox(options=options)
driver.get('https://demo.actitime.com/frontRedirector.do')
driver.implicitly_wait(30)
driver.find_element(By.ID,"username").send_keys('admin')
driver.find_element(By.NAME,"pwd").send_keys('manager')
driver.find_element(By.CLASS_NAME,'initial').click()
wait=WebDriverWait(driver=driver,timeout=30)
wait.until(expected_conditions.title_contains('Enter Time-Track'))

titl=driver.title
print('Title of page is:',titl)
driver.quit()

print('*************go to google and find number of links available using explicty wait************')

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from  selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
options=Options()
driver=webdriver.Firefox(options=options)
driver.get('https://google.com')
links=driver.find_elements(By.XPATH,'//a')
for i in range(0,len(links)):
    #print(links[i])
    link=links[i]
    txt=link.text
    print(txt)'''
import time

print('************* find number of checkbox available--Incomplete ************')
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
options=Options()
driver= webdriver.Chrome(options=options)
driver.get('https://www.google.com/gmail/about/')

driver.find_element(By.XPATH,'//a[text()="Sign in"]').click()
driver.implicitly_wait(30)
mail=driver.find_element(By.XPATH,'//input[@type="email"]')
mail.send_keys('geetanjali128@gmail.com')
wait=WebDriverWait(driver=driver,timeout=30)
wait.until(expected_conditions.title_contains('Gmail'))
mail.send_keys(Keys.ENTER)
time.sleep(20)
pwd=driver.find_element(By.XPATH,'//input[@type="password"]')
pwd.send_keys('Geeta128@')
pwd.click()




'''checkBoxes=driver.find_elements(By.XPATH,'//input')
for i in checkBoxes:
    checkbox=i.text
    print(checkbox)'''


driver.quit()
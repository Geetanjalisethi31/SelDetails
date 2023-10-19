'''print("*************MouseAction on a website******************************")
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import Firefox,ActionChains
options=Options()
driver=webdriver.Firefox(options=options)
driver.get('https://www.zoho.com/')
driver.implicitly_wait(20)
find_ele=driver.find_element(By.XPATH,'(//span[text()="Products"])[1]')

act=ActionChains(driver)
act.move_to_element(find_ele).click(find_ele).perform()

wait=WebDriverWait(driver=driver,timeout=20)
wait.until(expected_conditions.title_contains('Zoho | Cloud Software'))
find_ele2=driver.find_element(By.XPATH,'(//li[text()="Marketplace"])[1]')
act=ActionChains(driver)
act.move_to_element(find_ele2).click(find_ele2).perform()
driver.quit()
import time

print("*************MouseAction-Basic click on a website******************************")
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

options=Options()
driver=webdriver.Firefox(options=options)
driver.implicitly_wait(10)
driver.get('https://www.google.com')

ele=driver.find_element(By.LINK_TEXT,'Gmail')

time.sleep(10)
act=ActionChains(driver)
#act.context_click(ele).perform()
#act.double_click(ele).perform()
act.click(ele).perform()

time.sleep(10)
driver.quit()'''
import time

print("*************MouseAction-Drag and drop on a website******************************")
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
options=Options()
driver=webdriver.Firefox(options=options)
driver.implicitly_wait(20)
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
source=driver.find_element(By.XPATH,'(//div[text()="Stockholm"])[2]')
target=driver.find_element(By.XPATH,'//div[@id="box106"]')
act=ActionChains(driver)
act.drag_and_drop(source,target).perform()
source1=driver.find_element(By.XPATH,'(//div[text()="Washington"])[2]')
target1=driver.find_element(By.XPATH,'//div[@id="box107"]')
act.move_to_element(source1).click_and_hold(source1).move_to_element(target1).release().perform()

time.sleep(10)
driver.quit()

'''print("*************scroll in a page on a website******************************")

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
driver.get('https://www.geeksforgeeks.org/')
wait=WebDriverWait(driver=driver,timeout=30)
wait.until(expected_conditions.title_contains('Geeks'))
js_command='window.scroll(300,400)'
driver.execute_script(js_command)
driver.quit()'''
import time

print("*************pop-Up handle in a page on a website******************************")
'''print("*************click on 'Ok' button on the pop up on a website******************************")
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
options=Options()
driver=webdriver.Firefox(options=options)
driver.maximize_window()
driver.get('http://www.javascriptkit.com/javatutors/'
           'alert2.shtml')
driver.find_element(By.NAME,'B2').click()
time.sleep(10)
act=driver.switch_to.alert
act.accept()
driver.quit()

print("*************click on 'Cancel' button on confirm- pop up on a website******************************")

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
options=Options()
driver=webdriver.Firefox(options=options)
driver.get('http://javascriptkit.com/javatutors/alert2.shtml')
driver.find_element(By.NAME,'B3').click()
alt=driver.switch_to.alert
print(alt.text)
alt.dismiss()
driver.quit()

print("*************send values on the prompt pop up on a website******************************")

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
options=Options()
driver=webdriver.Firefox(options=options)
driver.get('http://javascriptkit.com/javatutors/alert2.shtml')
driver.find_element(By.NAME,'B4').click()
alt=driver.switch_to.alert
print(alt.text)
alt.send_keys('Geeta')
driver.quit()

print("*************To handle hidden pop up on a website-yatra.com******************************")


from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
options=Options()
driver=webdriver.Firefox(options=options)
driver.get('https://www.yatra.com/')
driver.find_element(By.ID,'BE_flight_origin_date').click()
time.sleep(20)
driver.find_element(By.ID,'29/09/2023').click()
time.sleep(10)
driver.quit()

print("*************To handle parent and child window******************************")

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

options=Options()
driver=webdriver.Firefox(options=options)
driver.maximize_window()
driver.get('https://demo.actitime.com/login.do')
driver.implicitly_wait(20)
driver.find_element(By.LINK_TEXT,'actiTIME Inc.').click()
#getting window handle ids
winow_handle_ids=driver.window_handles
print(winow_handle_ids)
parent_id=winow_handle_ids[0]
child_id=winow_handle_ids[1]
#switch to chils window
driver.switch_to.window(child_id)
time.sleep(20)
driver.find_element(By.LINK_TEXT,'Get started').click()
driver.switch_to.window(parent_id)
time.sleep(20)
driver.find_element(By.NAME,'username').send_keys('admin')
driver.find_element(By.NAME,'pwd')
driver.find_element(By.LINK_TEXT,'Login ').click()'''

print("*************To handle FRAMEs in a window******************************")

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

options=Options()
driver=webdriver.Firefox(options=options)
driver.maximize_window()
driver.get('https://www.hobo-web.co.uk/website-frames/')
#find the frame
all_Frame=driver.find_elements(By.TAG_NAME,'iframe')
d=len(all_Frame)

print(d)
#identify frame by id
frame_comp=driver.find_element(By.ID,"twitter-widget-0")
time.sleep(20)
#switch to a perticular frame
driver.switch_to.frame(frame_comp)
#click the frame
driver.find_element(By.ID,'follow-button').click()
time.sleep(20)
driver.quit()
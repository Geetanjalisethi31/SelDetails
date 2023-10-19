'''from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# instance of Options class allows
# us to configure Headless Chrome
options = Options()
# initializing webdriver for Chrome with our options
driver = webdriver.Firefox(options=options)

driver.get('https://www.google.co.in')
title_of_page=driver.title
print("Title of the page=",title_of_page)
driver.maximize_window()
driver.implicitly_wait(20)
time.sleep(2)
driver.quit()
print('*********************get size of window**************************')
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
options = Options()
driver=webdriver.Chrome(options=options)

driver.get("https://www.w3schools.com/")

driver.maximize_window()
driver.implicitly_wait('20')
size=driver.get_window_size()
print('size of the Window=',size)
print('type of size=',type(size))
height=size['height']
width=size['width']
print('Height=',height,'Width=',width)
driver.set_window_size(width=1200,height=800)
size2=driver.get_window_size()
print('Modified Size=',size2)

print('*********************************Position of window********************************')

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options=Options()
driver=webdriver.Chrome(options=options)
driver.get('https://mail.google.com/mail/u/0/#inbox')
positon=driver.get_window_position()
print('Position of the window=',positon)
x_axis=positon['x']
y_axis=positon['y']
print('X axis=',x_axis,'Y axis=',y_axis)
repostion=driver.set_window_position(x=20,y=30)
repostion2=driver.get_window_position()
print('Nwe size=',repostion2)

print('*********************************Back ,forward,Refresh, Current URL function********************************')

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import  By
import time
options=Options()
driver=webdriver.Chrome(options=options)
driver.get('https://www.w3schools.com/sql/sql_syntax.asp')
driver.maximize_window()
driver.implicitly_wait(60)
driver.back()
driver.implicitly_wait(30)
window_title=driver.title
print('title=',window_title)
driver.forward()
driver.implicitly_wait(30)
window_title2=driver.title
print('forward title=',window_title2)
currntUrl=driver.current_url
print('currentURl is=',currntUrl)
driver.refresh()
print('***************Go to google page and click on gmail link *click on a link********************************')
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
options=Options()
driver=webdriver.Firefox(options=options)
driver.maximize_window()
driver.get('https://www.google.com')
driver.implicitly_wait(30)
findElement=driver.find_element(By.NAME,'q')

findElement.send_keys('Java')
findElement1=driver.find_element(By.LINK_TEXT,'Gmail').click()
driver.quit()
import time

print('***************Basic action on elements********************************')
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
options=Options()
driver=webdriver.Firefox(options=options)
driver.maximize_window()
driver.get('https://google.com')
driver.implicitly_wait(40)
findEle=driver.find_element(By.NAME,'q')
findEle.send_keys('Java')
time.sleep(20)
findEle.send_keys(Keys.CONTROL,'a')
findEle.send_keys(Keys.BACKSPACE)
time.sleep(20)
findEle.send_keys('python')
import time

print("*****************************Perform log in action***************************************")
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
options=Options()
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://facebook.com')
driver.implicitly_wait(30)
uname=driver.find_element(By.XPATH,'//input[@id="email"]')
uname.send_keys('geetanjali128@gmail.com')
pword=driver.find_element(By.XPATH,'//input[@type="password"]')
pword.send_keys('Geeta128@',Keys.ENTER)
#time.sleep(30)
#driver.find_element(By.XPATH,'//button[@name="login"]').click()
import time

print('*******************Toget toot tip message***************************')
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
options=Options()
driver=webdriver.Firefox(options=options)
driver.get('https://google.com')
scrchbx=driver.find_element(By.XPATH,'//textarea[@name="q"]')
titlofbx=scrchbx.get_attribute('title')
print(titlofbx)
if titlofbx=='search':
    print('Pass')
else:
    print('Fail')

print('************************To check text box is email or password************************')
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from  selenium.webdriver.common.by import By
options=Options()
driver=webdriver.Firefox(options=options)
driver.get('https://google.com')
driver.implicitly_wait(30)
driver.find_element(By.LINK_TEXT,'Gmail').click()

driver.find_element(By.LINK_TEXT,'Sign in').click()
ele=driver.find_element(By.XPATH,'//input[@type="password"]')

atvalue=ele.get_attribute('type')
print(atvalue)

if atvalue=='email':
    print('Its a text area')
else:
    print('Something else')
driver.quit()
print('************************operations************************')

from selenium import  webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
options=Options()
driver=webdriver.Firefox(options=options)
driver.get(
)
scrchbx=driver.find_element(By.XPATH,'//textarea[@name="q"]')
chck=scrchbx.is_enabled()
if chck==True:
    print('Enabled')
else:
    print('Disabled')
chck2=scrchbx.is_displayed()
if chck2==True:
    print('display')
else:
    print('not')
lnth=scrchbx.get_attribute('maxlength')
print(lnth)

print(scrchbx.location)

print(scrchbx.size)
mail=driver.find_element(By.LINK_TEXT,'Gmail')
font=mail.value_of_css_property('font-size')
print('fontsize=',font)
family=mail.value_of_css_property('font-family')
print('fontfamily',family)

driver.quit()'''

print('************************Radio button selected or not************************')
from selenium import  webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
options=Options()
driver=webdriver.Firefox(options=options)
driver.get('https://demo.actitime.com/frontRedirector.do')
checkbx=driver.find_element(By.XPATH,'//input[@type="checkbox"]')


stats=checkbx.is_selected()
if stats==True:
    print('selected')
else:
    print('Not selected')
driver.quit()
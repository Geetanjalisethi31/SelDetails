'''print('*************************select dob in fb pge*****************************************')
from selenium import  webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

options=Options()
driver=webdriver.Firefox(options=options)
driver.maximize_window()
driver.get('https://www.facebook.com/r.php?locale=en_GB&display=page')
month=driver.find_element(By.ID,"month")
slt=Select(month)
slt.select_by_index(0)
day=driver.find_element(By.ID,"day")
day_slt=Select(day)
day_slt.select_by_value('25')
yr=driver.find_element(By.ID,'year')
yr_slct=Select(yr)
yr_slct.select_by_visible_text('2012')
#yr_slct.deselect_by_value('2012') only work when multiple options selected

print('*************************select Mulitiple ddl in fb pge*****************************************')
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
options=Options()
driver=webdriver.Firefox(options=options)
driver.maximize_window()
driver.get('https://www.facebook.com/r.php?locale=en_GB&display=page')
month=driver.find_element(By.ID,"month")
allmonth=Select(month)
multipl=allmonth.is_multiple
print(multipl)
txt=allmonth.options
print(txt)
for i in range(0,len(txt)):
    ttl=txt[i]
    titl=ttl.text
    #print(ttl,'is from index')will give the selenium.webdriver.remote.webelement.WebElement (session="644a089f-6e13-48e3-a3cb-3e02d873f6f9"
    # , element="aaba4905-d18d-4623-b484-d70a4889489a" for each month
    print(titl,'is title')
allmonth.select_by_visible_text('Jan')
seltmont=allmonth.first_selected_option

print('Selecetd month',seltmont.text)
driver.quit()


print('*************************Go to web page and perform action*****************************************')
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
options=Options()
driver=webdriver.Firefox(options=options)
driver.maximize_window()
driver.get('https://www.zoho.com/')
driver.find_element(By.XPATH,'(//span[text()="Products"])[1]').click()
wait=WebDriverWait(driver=driver,timeout=30)
wait.until(expected_conditions.title_contains('Zoho | Cloud Software'))
print('Title of the page is',driver.title)
driver.find_element(By.XPATH,'(//li[text()="Marketplace"])[1]')
driver.quit()'''
import time

print('*************************How to handle auto suggestion*****************************************')
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
options=Options()
driver=webdriver.Firefox(options=options)
driver.get('https://google.com/')
findEle=driver.find_element(By.NAME,'q')
findEle.send_keys('python')
time.sleep(10)
suggestion=driver.find_elements(By.XPATH,'//div[@class="pcTkSc"]')
size=len(suggestion)
print('Number of suggestions',size)
s=[]
for i in range(0,len(suggestion)):
    sug=suggestion[i]

    print(sug.text)
    if sug.text=='python compiler':
     sug.click()
     break;

driver.quit()

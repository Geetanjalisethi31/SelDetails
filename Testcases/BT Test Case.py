from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
import time
class test_login(TestCase):
    def test_landing_page(self):
        options = Options()
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
        # Launch of the application URL(https://www.bt.com/)
        driver.get('https://www.bt.com/')
        driver.implicitly_wait(20)
        frame = driver.find_element(By.CLASS_NAME, 'truste_popframe')
        driver.switch_to.frame(frame)
        # Close accept Cookie pop-up if it appears
        accept = driver.find_element(By.LINK_TEXT, 'Accept all cookies')
        accept.click()
        # Hover to Mobile menu
        driver.switch_to.default_content()
        ele = driver.find_element(By.XPATH, '(//span[text()="Mobile"])[1]')
        act = ActionChains(driver)
        act.move_to_element(ele).perform()
        time.sleep(30)
        # From mobile menu, select Mobile phones
        ele1 = driver.find_element(By.LINK_TEXT, 'Mobile phones')

        act = ActionChains(driver)
        act.move_to_element(ele1).click().perform()

        time.sleep(20)

        # Verify the numbers of banners present below “See Handset details” should not be less than 3
        num_banner=driver.find_elements(By.XPATH,'(//div[@class="flexpay-card_card_wrapper__Antym"])')
        num=len(num_banner)
        assert num>=3,'Less than 3'

        # Scroll down and click View SIM only deals
        scrolDown = 'window.scroll(1500,2000)'
        driver.execute_script(scrolDown)
        simOnlyOption = driver.find_element(By.LINK_TEXT, 'View SIM only deals')
        simOnlyOption.click()
        time.sleep(10)

        # Validate the title for new page.
        act_title_of_window = driver.title
        print(act_title_of_window)
        exp_title_of_window='SIM Only Deals | Compare SIMO Plans & Contracts | BT Mobile'
        assert act_title_of_window==exp_title_of_window,'Actual is not expected'
        # Validate “30% off and double data” was 125GB 250GB Essential Plan, was £27 £18.90 per month
        try:


            # Find the elements containing the plan details and prices
            plan_details_element = driver.find_element(By.XPATH, "//div[contains(text(), '30% off and double data')]")
            price_before_element = driver.find_element(By.XPATH, "//span[contains(text(), '£27')]")
            price_after_element = driver.find_element(By.XPATH, "//span[contains(text(), '£18.90')]")

            # Verify the text and prices
            plan_details_text = plan_details_element.text.strip()
            price_before_text = price_before_element.text.strip()
            price_after_text = price_after_element.text.strip()

            # Check if the text and prices match the expected values
            expected_plan_details = "30% off and double data"
            expected_price_before = "£27"
            expected_price_after = "£18.90"

            assert plan_details_text == expected_plan_details, f"Plan details do not match. Expected: {expected_plan_details}, Actual: {plan_details_text}"
            assert price_before_text == expected_price_before, f"Price before does not match. Expected: {expected_price_before}, Actual: {price_before_text}"
            assert price_after_text == expected_price_after, f"Price after does not match. Expected: {expected_price_after}, Actual: {price_after_text}"

            print("Validation successful: Text and prices match the expected values.")
        except Exception as e:
            print(f"Validation failed: {e}")

        finally:
            # Close the WebDriver
            driver.quit()




        #driver.quit()




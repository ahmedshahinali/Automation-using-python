import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains, Keys
import time
#import pytest
driver = webdriver.Chrome()

class Test(unittest.TestCase):

    def test_1(shop):
       
        url = "https://www.google.com"
        driver.get(url)
        driver.maximize_window()
        actions = ActionChains(driver)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea").send_keys("Etisalat")
        #actions.send_keys(keys.ENTER)
        actions.perform()
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click()
        driver.find_element(By.XPATH, "//*[contains(text(),'e& (etisalat and ) UAE | Mobile plans, TV & Internet plans, WiFi ...')]").click()
        driver.find_element(By.XPATH, "//*[contains(text(),'Devices')]").click()
        Samsung=driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[1]/nav/div/div/div[3]/div/div[1]/div/div/ul/li[3]/div/section/div/div/div[2]/div[2]/div[2]/a")
        actions.move_to_element(Samsung).perform()
        Samsung.click()
        driver.execute_script("window.scrollTo(0,300);")
        phones=driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div/div[3]/div/section/div[1]/div/div[1]/div/ul/li[2]")
        actions.move_to_element(phones).perform()
        phones.click()
        driver.execute_script("window.scrollTo(0,700);")
        time.sleep(2)
        S24=driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div/div[3]/div/div[2]/section/div/div/div[2]/div/div/div[3]/div/div/a")
        actions.move_to_element(S24).perform()
        S24.click()
        time.sleep(2)
        storage=driver.find_element(By.XPATH, "//*[contains(text(),'256GB')]")
        actions.move_to_element(storage).perform()
        storage.click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,700);")
        time.sleep(2)
        driver.find_element(By.ID, "configure").click
        #CART=driver.find_element(By.XPATH, "/html/body/div[1]/ui-view/device-configuration-component/section/div/div/div[3]/price-details/div/div/div[3]/div/div[2]/ng-container[7]/div/div[2]")
        #driver.execute_script("window.scrollTo(0,300);")
        #actions.move_to_element(CART).perform()
        time.sleep(2)
        #CART.click()
        time.sleep(2)
        last=driver.find_element(By.XPATH, "//*[contains(text(),'S24')]")
        print(last.text," Test passed  ")
        shop.assertEqual(last.text, "")
        time.sleep(2)
        driver.quit() 
    
#shop = Test()
#shop.test_1()


# print(last.text," please run the (python -m unittest Etisalat_shop.py) command to run the TC to run it comment the last 2 lines  ")

    
     
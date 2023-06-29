# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSam():
  def setup_method(self, method):
    capabilities = {
    "name" : "TEST",
    "browserName": "chrome",
    "browserVersion": "114.0",
    "selenoid:options": {
        "enableVideo": False
        ,"enableVNC": True
      }
   }
    self.driver = webdriver.Remote(command_executor='http://localhost:4448/', desired_capabilities=capabilities)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_sam(self):
    # Test name: sam
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://www.google.co.th/")
    # 2 | click | id=APjFqb | 
    self.driver.find_element(By.ID, "APjFqb").click()
    # 3 | type | id=APjFqb | selenoid
    self.driver.find_element(By.ID, "APjFqb").send_keys("selenoid")
    # 4 | click | name=btnK | 
    time.sleep(1)
    self.driver.find_element(By.NAME, "btnK").click()
    time.sleep(1)
    # 5 | waitForElementPresent | css=.hlcw0c:nth-child(1) > .MjjYud > div | 30000
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".hlcw0c:nth-child(1) > .MjjYud > div")))
    time.sleep(1)
    # 6 | close |  | 
    self.driver.close()
  

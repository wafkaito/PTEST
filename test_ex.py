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
from selenium.webdriver.chrome.options import Options

class TestEx():
  def setup_method(self, method):
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Enable headless mode
    self.driver = webdriver.Remote(
        command_executor='http://10.99.20.131:4448',
        options=chrome_options
    )
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_ex(self):
    self.driver.get("https://www.google.co.th/")
    self.driver.set_window_size(1536, 816)
    time.sleep(1)
    self.driver.find_element(By.ID, "APjFqb").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "APjFqb").send_keys("selenium grid")
    time.sleep(1)
    self.driver.find_element(By.NAME, "btnK").click()
    time.sleep(1)
    self.driver.close()

  

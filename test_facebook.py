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

class TestFacebook():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_facebook(self):
    self.driver.get("https://www.google.co.th/")
    self.driver.set_window_size(792, 816)
    self.driver.find_element(By.ID, "APjFqb").send_keys("facebook")
    time.sleep(2)
    self.driver.find_element(By.NAME, "btnK").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".tF2Cxc > .yuRUbf .LC20lb").click()
    time.sleep(5)
    self.driver.find_element(By.NAME, "login").click()
    time.sleep(2)
    self.driver.find_element(By.ID, "email").send_keys("waf")
    time.sleep(2)
    self.driver.find_element(By.ID, "pass").click()
    time.sleep(2)
    self.driver.find_element(By.ID, "pass").send_keys("waf")
    time.sleep(2)
    self.driver.find_element(By.ID, "loginbutton").click()
    time.sleep(5)
    self.driver.close()
  

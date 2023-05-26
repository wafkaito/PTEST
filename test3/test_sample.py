from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def test_start():
    global driver
    driver = webdriver.Chrome(executable_path= "driver/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

def test_login():
    username=driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")
    username.send_keys("Admin")
    password=driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input")
    password.send_keys("admin123")
    driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
def test_leardown():
    time.sleep(10)
    driver.close
    driver.quit


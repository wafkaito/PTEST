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

class Test1():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://192.168.41.66:4445', desired_capabilities=DesiredCapabilities.CHROME)
    self.driver.maximize_window()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_1(self):
    print("`set speed` is a no-op in code export, use `pause` instead")
    time.sleep(10)
    self.driver.get("https://demo.irplus.in.th/Listed/susco/home.asp")
    self.driver.find_element(By.LINK_TEXT, "TH").click()
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    self.driver.find_element(By.LINK_TEXT, "หน้าหลักนักลงทุนสัมพันธ์").click()
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลทางการเงิน")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "งบการเงิน").click()
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลทางการเงิน")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "ข้อมูลสำคัญทางการเงิน").click()
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลทางการเงิน")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "คำอธิบายและการวิเคราะห์").click()
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลทางการเงิน")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "รายงานประจำปี").click()
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลทางการเงิน")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "ฟอร์ม 56-1").click()
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลทางการเงิน")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.LINK_TEXT, "หนังสือชี้ชวน").click()
    self.vars["win2199"] = self.wait_for_window(2000)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win2199"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
    element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลราคาหลักทรัพย์")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "ราคาหลักทรัพย์").click()
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลราคาหลักทรัพย์")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "ราคาหลักทรัพย์ย้อนหลัง").click()
    self.driver.execute_script("window.history.go(-1)")
    print("`set speed` is a no-op in code export, use `pause` instead")
    self.driver.get("https://demo.irplus.in.th/Listed/susco/home.asp")
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "TH").click()
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลราคาหลักทรัพย์")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "เครื่องคำนวณการลงทุน").click()
    print("`set speed` is a no-op in code export, use `pause` instead")
    self.driver.get("https://demo.irplus.in.th/Listed/susco/home.asp")
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "TH").click()
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลสำหรับผู้ถือหุ้น")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "ข้อมูลสำหรับผู้ถือใบสำคัญแสดงสิทธิ").click()
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลสำหรับผู้ถือหุ้น")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "โครงสร้างผู้ถือหุ้น").click()
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลสำหรับผู้ถือหุ้น")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "การประชุมผู้ถือหุ้น").click()
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลสำหรับผู้ถือหุ้น")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "นโยบายจ่ายเงินปันผล").click()
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลสำหรับผู้ถือหุ้น")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "สรุปข้อสนเทศ").click()
    self.driver.execute_script("window.history.go(-1)")
    print("`set speed` is a no-op in code export, use `pause` instead")
    self.driver.get("https://demo.irplus.in.th/Listed/susco/home.asp")
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "TH").click()
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    self.driver.find_element(By.LINK_TEXT, "ปฎิทินกิจกรรม").click()
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "ข้อมูลนำเสนอแบบมัลติมีเดีย").click()
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    self.driver.find_element(By.LINK_TEXT, "ข้อมูลบทวิเคราะห์").click()
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    element = self.driver.find_element(By.LINK_TEXT, "ข่าวสารบริษัท")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "ข่าวแจ้งตลาดหลักทรัพย์").click()
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    time.sleep(1)
    element = self.driver.find_element(By.LINK_TEXT, "ข่าวสารบริษัท")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "ข่าวสารล่าสุด").click()
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    element = self.driver.find_element(By.LINK_TEXT, "ข่าวสารบริษัท")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "ข่าวจากสื่อสิ่งพิมพ์").click()
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    time.sleep(1)
    element = self.driver.find_element(By.LINK_TEXT, "ข่าวสารบริษัท")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "ข่าวประชาสัมพันธ์").click()
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    element = self.driver.find_element(By.LINK_TEXT, "สอบถามข้อมูล")
    time.sleep(5)
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "ข่าวสารทางอีเมล").click()
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    element = self.driver.find_element(By.LINK_TEXT, "สอบถามข้อมูล")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "ฝากคำถาม").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    element = self.driver.find_element(By.LINK_TEXT, "สอบถามข้อมูล")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "คำถามที่ถูกถามบ่อย").click()
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    time.sleep(1)
    element = self.driver.find_element(By.LINK_TEXT, "สอบถามข้อมูล")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "ช่องทางการรับเรื่องร้องเรียน").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    self.driver.find_element(By.LINK_TEXT, "ติดต่อนักลงทุนสัมพันธ์").click()
    self.driver.get("https://demo.irplus.in.th/Listed/susco/home.asp")
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "TH").click()
    self.driver.find_element(By.LINK_TEXT, "ส่งเสริมการขาย").click()
    time.sleep(3)
    self.driver.find_element(By.LINK_TEXT, "ผลิตภัณฑ์และบริการ").click()
    self.driver.find_element(By.LINK_TEXT, "น้ำมันเครื่อง").click()
    time.sleep(3)
    self.driver.find_element(By.LINK_TEXT, "ผลิตภัณฑ์และบริการ").click()
    self.driver.find_element(By.LINK_TEXT, "สถานีบริการ").click()
    time.sleep(3)
    self.driver.find_element(By.LINK_TEXT, "ผลิตภัณฑ์และบริการ").click()
    self.driver.find_element(By.XPATH, "//a[contains(@href, \'susco-square-stations.asp\')]").click()
    time.sleep(5)
    self.driver.find_element(By.ID, "navbarDropdown").click()
    self.driver.find_element(By.LINK_TEXT, "สารจากประธานกรรมการ").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "navbarDropdown").click()
    self.driver.find_element(By.LINK_TEXT, "ความเป็นมา").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "navbarDropdown").click()
    self.driver.find_element(By.LINK_TEXT, "วิสัยทัศน์ / พันธกิจ").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "navbarDropdown").click()
    self.driver.find_element(By.LINK_TEXT, "โครงสร้างธุรกิจ").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "navbarDropdown").click()
    self.driver.find_element(By.LINK_TEXT, "คณะกรรมการบริษัท").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "navbarDropdown").click()
    self.driver.find_element(By.LINK_TEXT, "คณะผู้บริหาร").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "navbarDropdown").click()
    self.driver.find_element(By.LINK_TEXT, "โครงสร้างการจัดการ").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "navbarDropdown").click()
    self.driver.find_element(By.LINK_TEXT, "ความรับผิดชอบต่อสังคม").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "navbarDropdown").click()
    self.driver.find_element(By.LINK_TEXT, "การกำกับดูแลกิจการ").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "navbarDropdown").click()
    self.driver.find_element(By.LINK_TEXT, "โครงการในอนาคต").click()
    time.sleep(3)
    print("`set speed` is a no-op in code export, use `pause` instead")
    self.driver.find_element(By.LINK_TEXT, "หน้าหลัก").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fa").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "EN").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fa").click()
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dropdown-menu-right > li:nth-child(1) > .dropdown-item").click()
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".dropdown-menu-right > li:nth-child(2) > .dropdown-item")
    time.sleep(1)
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) li:nth-child(1) > .dropdown-item").click()
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".dropdown-menu-right > li:nth-child(2) > .dropdown-item")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) li:nth-child(2) > .dropdown-item").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".dropdown-menu-right > li:nth-child(2) > .dropdown-item")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "MD&A").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    time.sleep(1)
    element = self.driver.find_element(By.CSS_SELECTOR, ".dropdown-menu-right > li:nth-child(2) > .dropdown-item")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) li:nth-child(4) > .dropdown-item").click()
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".dropdown-menu-right > li:nth-child(2) > .dropdown-item")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) li:nth-child(5) > .dropdown-item").click()
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    time.sleep(1)
    element = self.driver.find_element(By.CSS_SELECTOR, ".dropdown-menu-right > li:nth-child(2) > .dropdown-item")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, ".submenu > li:nth-child(6) > .dropdown-item").click()
    self.vars["win4143"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win4143"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
    time.sleep(5)
    print("`set speed` is a no-op in code export, use `pause` instead")
    self.driver.get("https://demo.irplus.in.th/Listed/susco/home.asp")
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "EN").click()
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".dropdown-menu-right > li:nth-child(3) > .dropdown-item")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) li:nth-child(1) > .dropdown-item").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".dropdown-menu-right > li:nth-child(3) > .dropdown-item")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) li:nth-child(2) > .dropdown-item").click()
    self.driver.execute_script("window.history.go(-1)")
    time.sleep(1)
    print("`set speed` is a no-op in code export, use `pause` instead")
    self.driver.get("https://demo.irplus.in.th/Listed/susco/home.asp")
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "EN").click()
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".dropdown-menu-right > li:nth-child(3) > .dropdown-item")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) li:nth-child(3) > .dropdown-item").click()
    self.driver.get("https://demo.irplus.in.th/Listed/susco/home.asp")
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "EN").click()
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > .dropdown-toggle")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) li:nth-child(1) > .dropdown-item").click()
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > .dropdown-toggle")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) li:nth-child(2) > .dropdown-item").click()
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > .dropdown-toggle")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) li:nth-child(3) > .dropdown-item").click()
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    time.sleep(1)
    element = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > .dropdown-toggle")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) li:nth-child(4) > .dropdown-item").click()
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    time.sleep(1)
    element = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > .dropdown-toggle")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) li:nth-child(5) > .dropdown-item").click()
    time.sleep(1)
    self.driver.execute_script("window.history.go(-1)")
    print("`set speed` is a no-op in code export, use `pause` instead")
    self.driver.get("https://demo.irplus.in.th/Listed/susco/home.asp")
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "EN").click()
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dropdown-menu-right > li:nth-child(5) > .dropdown-item").click()
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dropdown-menu-right > li:nth-child(6) > .dropdown-item").click()
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(7) > .dropdown-item").click()
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    time.sleep(5)
    print("`set speed` is a no-op in code export, use `pause` instead")
    self.driver.get("https://demo.irplus.in.th/Listed/susco/home.asp")
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "EN").click()
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(8) > .dropdown-item")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(8) li:nth-child(1) > .dropdown-item").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(8) > .dropdown-item")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(8) li:nth-child(2) > .dropdown-item").click()
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(8) > .dropdown-item")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(8) li:nth-child(3) > .dropdown-item").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(8) > .dropdown-item")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(8) li:nth-child(4) > .dropdown-item").click()
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(9) > .dropdown-item")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(9) li:nth-child(1) > .dropdown-item").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(9) > .dropdown-item")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(9) li:nth-child(2) > .dropdown-item").click()
    print("`set speed` is a no-op in code export, use `pause` instead")
    self.driver.get("https://demo.irplus.in.th/Listed/susco/home.asp")
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "EN").click()
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(9) > .dropdown-item")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(9) li:nth-child(3) > .dropdown-item").click()
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(9) > .dropdown-item")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(9) li:nth-child(4) > .dropdown-item").click()
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(10) > .dropdown-item").click()
    print("`set speed` is a no-op in code export, use `pause` instead")
    self.driver.get("https://demo.irplus.in.th/Listed/susco/home.asp")
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "EN").click()
    self.driver.find_element(By.LINK_TEXT, "PROMOTIONS").click()
    time.sleep(3)
    self.driver.find_element(By.LINK_TEXT, "PRODUCTS SERVICE").click()
    self.driver.find_element(By.LINK_TEXT, "OIL").click()
    time.sleep(3)
    self.driver.find_element(By.LINK_TEXT, "PRODUCTS SERVICE").click()
    self.driver.find_element(By.LINK_TEXT, "STATIONS").click()
    time.sleep(3)
    self.driver.find_element(By.LINK_TEXT, "PRODUCTS SERVICE").click()
    self.driver.find_element(By.XPATH, "//li[3]/div/a[3]").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "navbarDropdown").click()
    self.driver.find_element(By.LINK_TEXT, "CHAIRMAN\'S MESSAGE").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "navbarDropdown").click()
    self.driver.find_element(By.LINK_TEXT, "HISTORY").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "navbarDropdown").click()
    self.driver.find_element(By.LINK_TEXT, "VISION / MISSION").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "navbarDropdown").click()
    self.driver.find_element(By.LINK_TEXT, "BUSINESS STRUCTURE").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "navbarDropdown").click()
    self.driver.find_element(By.LINK_TEXT, "BOARD OF DIRECTORS").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "navbarDropdown").click()
    self.driver.find_element(By.LINK_TEXT, "MANAGEMENT TEAM").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "navbarDropdown").click()
    self.driver.find_element(By.LINK_TEXT, "ORGANIZATIONAL STRUCTURE").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "navbarDropdown").click()
    self.driver.find_element(By.LINK_TEXT, "CSR").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "navbarDropdown").click()
    self.driver.find_element(By.XPATH, "//a[9]").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "navbarDropdown").click()
    self.driver.find_element(By.XPATH, "//a[contains(text(),\'FUTURE INVESTMENT\')]").click()
    time.sleep(3)
    self.driver.find_element(By.LINK_TEXT, "HOME").click()

  

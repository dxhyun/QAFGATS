# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class SearchToItem(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/Python27/chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_search_to_item(self):
        driver = self.driver
        # Log-In Class
        driver.get("https://www.fashiongo.net/")
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[1]/ul[1]/li[2]/a").click()
        driver.find_element_by_id("email-inp").click()
        driver.find_element_by_id("email-inp").clear()
        driver.find_element_by_id("email-inp").send_keys("ma********@**********.***")
        driver.find_element_by_id("pwd_inp").click()
        driver.find_element_by_id("pwd_inp").clear()
        driver.find_element_by_id("pwd_inp").send_keys("K************")
        driver.find_element_by_name("loginRequestData").submit()

        # Search Class
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[1]/div[3]/form/input[1]").click()
        driver.find_element_by_id("lb_sch").send_keys("zenana")
        driver.find_element_by_id("ac_form1").submit()

        # 검색결과가 0인지 검증한다 pass이면 성공, error이면 실패이다 
        self.assertNotEqual("0 results for \"zenana\"", driver.find_element_by_xpath("/html/body/div[1]/div[10]/div[2]/div[2]/div/div[1]/div/p").text)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

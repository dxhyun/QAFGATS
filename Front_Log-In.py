# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class LogIn(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/Python27/chromedriver.exe')
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_log_in(self):
        driver = self.driver
        driver.get("https://www.fashiongo.net/")
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[1]/ul[1]/li[2]/a").click()
        driver.find_element_by_id("email-inp").click()
        driver.find_element_by_id("email-inp").clear()
        driver.find_element_by_id("email-inp").send_keys("ma********@**********.***")
        driver.find_element_by_id("pwd_inp").click()
        driver.find_element_by_id("pwd_inp").clear()
        driver.find_element_by_id("pwd_inp").send_keys("K**************")
        driver.find_element_by_name("loginRequestData").submit()
    
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

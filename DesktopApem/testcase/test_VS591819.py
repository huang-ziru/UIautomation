# coding = utf-8
import configparser, os
import time
from logging import Logger
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.color import Color
from framework.common import Common
from selenium.webdriver.common.by import By
class Testtitle_bar():
    def test_DarkMode(self, browser):
        browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='settings']").click()
        switch = browser.find_element(By.XPATH, "//div[@class='show-navigation'][4]/div/div[2]/mat-slide-toggle")
        if switch.find_element(By.TAG_NAME, 'input').get_attribute('aria-checked') == 'false':
            Common(browser).eleclick(switch)
        time.sleep(5)
        backcolor = browser.find_element(By.XPATH, "//body").value_of_css_property('background-color')
        assert Color.from_string(backcolor) == Color.from_string('#2a2a2a')
        textcolor = browser.find_element(By.XPATH, "//body").value_of_css_property('color')
        assert Color.from_string(textcolor) == Color.from_string('#fff')
        browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='settings']").click()
        switch = browser.find_element(By.XPATH, "//div[@class='show-navigation'][4]/div/div[2]/mat-slide-toggle")
        if switch.find_element(By.TAG_NAME, 'input').get_attribute('aria-checked') == 'true':
            Common(browser).eleclick(switch)
        time.sleep(5)

    def test_diffuser(self):
        config = configparser.ConfigParser()
        dirname = os.path.dirname(os.path.abspath(__file__))
        path = dirname + '/../framework/config.ini'
        config.read(path)
        browser_name = config.get('Browser', 'browser')
        if browser_name == 'Chrome':
            s = Service(r'..\framework\chromedriver.exe')
            self.driver = webdriver.Chrome(service=s)
            self.driver.maximize_window()
        elif browser_name == 'Edge':
            self.driver = webdriver.Edge(r'..\framework\msedgedriver.exe')
            self.driver.maximize_window()
        else:
            Logger.error('Do not support the Browser')
        servername = config.get('login', 'servername')
        url = "http://qapart:QQQaaa000@" + servername + "/ApemMobile/#/login"
        self.driver.get(url)
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("corp\\qapart")
        self.driver.find_element(By.XPATH, '//*[@id="mat-input-1"]').send_keys("QQQaaa000")
        self.driver.find_element(By.ID, 'signInBtn').click()
        backcolor = self.driver.find_element(By.XPATH, "//body").value_of_css_property('background-color')
        try:
            assert Color.from_string(backcolor) != Color.from_string('#2a2a2a')
            assert "theme-light" in self.driver.find_element(By.XPATH, "//body").get_attribute("class")
        finally:
            self.driver.quit()
    def test_offDarkMode(self, browser):
        browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='settings']").click()
        switch = browser.find_element(By.XPATH, "//div[@class='show-navigation'][4]/div/div[2]/mat-slide-toggle")
        if switch.find_element(By.TAG_NAME, 'input').get_attribute('aria-checked') == 'true':
            Common(browser).eleclick(switch)
        time.sleep(5)
        assert "theme-light" in browser.find_element(By.XPATH, "//body").get_attribute("class")




if __name__ == '__main__':
    pytest.main(["-s", "test_VS591819.py"])


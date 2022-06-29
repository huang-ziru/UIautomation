# coding = utf-8
import configparser
import time
from logging import Logger

import pytest
from selenium import webdriver
from selenium.webdriver.support.color import Color

from framework.basefunc import MainPage
class Testtitle_bar():
    @pytest.mark.run(order=1)
    def test_DarkMode(self, browser):
        elementObj = browser.find_element_by_xpath("/html/body/app-root/div/app-navigation")
        browser.execute_script("arguments[0].className='show-nav'", elementObj)
        time.sleep(2)
        browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='settings']").click()
        switch = browser.find_element_by_xpath("//div[@class='show-navigation'][4]/div/div[2]/mat-slide-toggle")
        if switch.find_element_by_tag_name('input').get_attribute('aria-checked') == 'false':
            MainPage(browser).eleclick(switch)
        time.sleep(5)
        backcolor = browser.find_element_by_xpath("//body").value_of_css_property('background-color')
        assert Color.from_string(backcolor) == Color.from_string('#2a2a2a')
        textcolor = browser.find_element_by_xpath("//body").value_of_css_property('color')
        assert Color.from_string(textcolor) == Color.from_string('#fff')

    @pytest.mark.run(order=2)
    def test_diffuser(self):
        desire_cap = {
            "platformName": "Android",
            "platformVersion": "10",
            "deviceName": "6NDNU21227203586",
            "noReset": "true",
            "browserName": "Chrome",
            "forceMjsonwp": "true",
            "chromedriverExecutable": r"F:\Python\Lib\site-packages\appium\webdriver\chromedriver.exe",
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        time.sleep(5)
        config = configparser.ConfigParser()
        path = r'..\framework\config.ini'
        config.read(path)
        servername = config.get('login', 'servername')
        url = "http://qapart:QQQaaa000@" + servername + ".qae.aspentech.com/ApemMobile/#/login"
        self.driver.get(url)
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys("corp\\huangzi")
        self.driver.find_element_by_xpath('//*[@id="mat-input-1"]').send_keys("hzrLove1213")
        self.driver.find_element_by_id('signInBtn').click()
        backcolor = self.driver.find_element_by_xpath("//body").value_of_css_property('background-color')
        try:
            assert Color.from_string(backcolor) != Color.from_string('#2a2a2a')
            assert "theme-light" in self.driver.find_element_by_xpath("//body").get_attribute("class")
        finally:
            self.driver.quit()

    @pytest.mark.run(order=3)
    def test_offDarkMode(self, browser):
        elementObj = browser.find_element_by_xpath("/html/body/app-root/div/app-navigation")
        browser.execute_script("arguments[0].className='show-nav'", elementObj)
        time.sleep(2)
        browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='settings']").click()
        switch = browser.find_element_by_xpath("//div[@class='show-navigation'][4]/div/div[2]/mat-slide-toggle")
        if switch.find_element_by_tag_name('input').get_attribute('aria-checked') == 'true':
            MainPage(browser).eleclick(switch)
        time.sleep(5)
        assert "theme-light" in browser.find_element_by_xpath("//body").get_attribute("class")




if __name__ == '__main__':
    pytest.main(["-s", "test_VS591819.py"])


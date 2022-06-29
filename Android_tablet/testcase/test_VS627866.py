# coding = utf-8
import time
from selenium.webdriver.support.color import Color
from framework.basefunc import MainPage
import pytest

def Check_hoverColor(browser,mode):
    elementObj = browser.find_element_by_xpath("/html/body/app-root/div/app-navigation")
    browser.execute_script("arguments[0].className='show-nav'", elementObj)
    time.sleep(2)
    browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='settings']").click()
    switch = browser.find_element_by_xpath("//div[@class='show-navigation'][4]/div/div[2]/mat-slide-toggle")
    if mode == 'dark':
        if switch.find_element_by_tag_name('input').get_attribute('aria-checked') == 'false':
            MainPage(browser).eleclick(switch)
    else:
        if switch.find_element_by_tag_name('input').get_attribute('aria-checked') == 'true':
            MainPage(browser).eleclick(switch)
    time.sleep(2)
    elementObj = browser.find_element_by_xpath("/html/body/app-root/div/app-navigation")
    browser.execute_script("arguments[0].className='show-nav'", elementObj)
    time.sleep(2)
    browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='process_order']").click()
    time.sleep(3)
    browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='refresh']").click()
    time.sleep(3)
    order_ele = browser.find_element_by_xpath("//div[contains(text(),'2BPLS')]")
    order_ele.click()
    time.sleep(3)
    phase_ele = browser.find_element_by_xpath("//button[@aria-label='Toggle PHASE57']")
    MainPage(browser).eleclick(phase_ele)
    time.sleep(2)
    # the background color turns to dark grey (rgb(55,55,55))
    field = browser.find_elements_by_xpath("//li/div/div/mat-form-field")[0]
    MainPage(browser).eleclick(field)
    param_color = browser.find_elements_by_xpath("//li")[0].value_of_css_property('background-color')
    return param_color

def test_CheckdiffMode(browser):
    time.sleep(4)
    param_color1 = Check_hoverColor(browser, 'dark')
    assert Color.from_string(param_color1) == Color.from_string('rgb(55,55,55)')
    param_color2 = Check_hoverColor(browser, 'light')
    assert Color.from_string(param_color2) == Color.from_string('rgb(228,240,250)')










if __name__ == '__main__':
    pytest.main(["-s", "test_VS627866.py"])
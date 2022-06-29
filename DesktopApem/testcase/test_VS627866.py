# coding = utf-8
import time
from selenium.webdriver.support.color import Color
from framework.common import Common
import pytest
from selenium.webdriver.common.by import By
def Check_hoverColor(browser,mode):
    browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='settings']").click()
    switch = browser.find_element(By.XPATH, "//div[@class='show-navigation'][4]/div/div[2]/mat-slide-toggle")
    if mode == 'dark':
        if switch.find_element(By.TAG_NAME, 'input').get_attribute('aria-checked') == 'false':
            Common(browser).eleclick(switch)
    else:
        if switch.find_element(By.TAG_NAME, 'input').get_attribute('aria-checked') == 'true':
            Common(browser).eleclick(switch)
    time.sleep(2)
    browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='process_order']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='refresh']").click()
    time.sleep(3)
    order_ele = browser.find_element(By.XPATH, "//div[contains(text(),'2BPLS')]")
    order_ele.click()
    time.sleep(3)
    phase_ele = browser.find_element(By.XPATH, "//button[@aria-label='Toggle PHASE57']")
    Common(browser).eleclick(phase_ele)
    time.sleep(2)
    # the background color turns to dark grey (rgb(55,55,55))
    field = browser.find_elements(By.XPATH, "//li/div/div/mat-form-field")[0]
    Common(browser).eleclick(field)
    param_color = browser.find_elements(By.XPATH, "//li")[0].value_of_css_property('background-color')
    return param_color
def test_CheckdiffMode(browser):
    time.sleep(4)
    param_color1 = Check_hoverColor(browser, 'dark')
    assert Color.from_string(param_color1) == Color.from_string('rgb(55,55,55)')
    param_color2 = Check_hoverColor(browser, 'light')
    assert Color.from_string(param_color2) == Color.from_string('rgb(228,240,250)')










if __name__ == '__main__':
    pytest.main(["-s", "test_VS627866.py"])
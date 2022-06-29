# coding = utf-8
import configparser
import time
from framework.basefunc import MainPage
import pytest
from selenium.webdriver import ActionChains
def dialog_text(browser):
    config = configparser.ConfigParser()
    path = r'..\framework\config.ini'
    # open the config.ini and get the data
    config.read(path)
    password = config.get('login', 'password')
    browser.find_element_by_xpath("//div/textarea").send_keys('234567')
    time.sleep(2)
    browser.find_element_by_xpath("//*[@id='dialog']/div/div[1]/form/mat-form-field[3]/div/div[1]/div[1]/input").send_keys(password)
    time.sleep(2)
def test_Toolbar(browser):
    time.sleep(4)
    order_ele = browser.find_element_by_xpath("//div[contains(text(),'START')]/../..")
    order_ele.find_elements_by_tag_name("td")[-1].click()
    time.sleep(5)
    phase_ele = browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='phase_state_executing']")
    phase_name = phase_ele.find_element_by_xpath("./../../../../../td[2]/div[1]/div").text
    MainPage(browser).eleclick(phase_ele)
    time.sleep(5)
    # Check the initial position is in the top center
    toolbar = browser.find_element_by_xpath("//*[@id='toolbar']/div")
    rect = toolbar.rect
    body = browser.find_element_by_xpath("/html/body")
    body_rect=body.rect
    toolbar_w = rect['x']+rect['width']/2
    assert abs(body_rect['width']/2 - toolbar_w) <= 20
    #  click and drag the left-most icon
    """待解决"""
    # toolbar_drag = browser.find_element_by_xpath("//div[@class='cdk-drag box']")
    # ActionChains(browser).drag_and_drop_by_offset(toolbar_drag, 10, 10).perform()
    # time.sleep(5)
    # browser.get_screenshot_as_file(r"..\\report\\result_picture\\toolbar_drag.png")
    # collapse the toolbar
    browser.find_element_by_xpath("//*[@id='toolbar']/div/button[3]").click()
    time.sleep(2)
    assert browser.find_element_by_xpath("//*[@id='toolbar']/div/button[1]").value_of_css_property('display') == 'none'
    assert browser.find_element_by_xpath("//*[@id='toolbar']/div/button[2]").value_of_css_property('display') == 'none'
    time.sleep(2)
    # expand the toolbar
    browser.find_element_by_xpath("//*[@id='toolbar']/div/button[3]").click()
    time.sleep(2)
    assert browser.find_element_by_xpath("//*[@id='toolbar']/div/button[1]").value_of_css_property('display') == 'block'
    assert browser.find_element_by_xpath("//*[@id='toolbar']/div/button[2]").value_of_css_property('display') == 'block'
    # Check the comments icon can work as expected
    browser.find_element_by_xpath("//*[@id='toolbar']/div/button[2]").click()
    time.sleep(1)
    assert MainPage(browser).is_element_showed("div#dialog") is True
    dialog_text(browser)
    MainPage(browser).eleclick(browser.find_element_by_xpath("//*[@id='toolbar']/div/button[1]"))
    time.sleep(5)
    assert 'execution' in browser.current_url
    MainPage(browser).eleclick(browser.find_element_by_xpath("//*[@id='toolbar']/div/button[2]"))
    time.sleep(3)
    dialog_text(browser)
    MainPage(browser).eleclick(browser.find_element_by_xpath("//*[@id='dialog']/div/div[2]/button[1]"))
    time.sleep(5)
    assert 'execution' in browser.current_url
    # Check the "Interrupt" icon can work as expected
    MainPage(browser).eleclick(browser.find_element_by_xpath("//*[@id='toolbar']/div/button[1]"))
    time.sleep(2)
    # a confirmation dialog will pops up
    assert MainPage(browser).is_element_showed("div#dialog") is True
    dialog_text(browser)
    MainPage(browser).eleclick(browser.find_element_by_xpath("//*[@id='dialog']/div/div[2]/button[2]"))
    time.sleep(5)
    assert 'execution' in browser.current_url
    # Can go back to tracking page, the phase state is interrupt.
    MainPage(browser).eleclick(browser.find_element_by_xpath("//*[@id='toolbar']/div/button[1]"))
    time.sleep(2)
    dialog_text(browser)
    MainPage(browser).eleclick(browser.find_element_by_xpath("//*[@id='dialog']/div/div[2]/button[1]"))
    time.sleep(5)
    assert 'tracking' in browser.current_url
    phase_path = "//div[@class='phase-name-text' and text()=\'"+phase_name+"\']/../../../td[3]"
    phase_ele = browser.find_element_by_xpath(phase_path)
    phase_state = phase_ele.get_attribute('textContent')
    assert 'Interrupted' == phase_state

if __name__ == '__main__':
    pytest.main(["-s", "test_VS628342.py"])
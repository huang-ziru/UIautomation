# coding = utf-8
import time
from framework.basefunc import MainPage
import pytest
def open_paramPage(browser):
    browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='refresh']").click()
    time.sleep(5)
    order_ele = browser.find_element_by_xpath("//div[contains(text(),'2BPLS')]")
    order_ele.click()
    time.sleep(3)
    # make some changes
    phase_ele = browser.find_element_by_xpath("//button[@aria-label='Toggle PHASE57']")
    MainPage(browser).eleclick(phase_ele)
    param_input = browser.find_element_by_xpath("//span[contains(text(),'TEMP')]/../mat-form-field/div/div/div/input")
    return param_input

def test_ParaPage(browser):
    param_input1 = open_paramPage(browser)
    before_change = param_input1.get_attribute("value")
    param_input1.clear()
    param_input1.send_keys('111')
    time.sleep(2)
    # click 'OK' and Uncheck the check box,then click 'ok'
    MainPage(browser).eleclick(browser.find_element_by_xpath("//span[text()=' OK ']/.."))
    time.sleep(3)
    assert MainPage(browser).is_element_showed("#audit-dialog") is True
    browser.find_element_by_xpath("//*[@id='audit-dialog']/div/div[2]/mat-form-field/div/div/div/textarea").send_keys('for test')
    browser.find_element_by_xpath("//span[text()='OK']/..").click()
    time.sleep(2)
    param_input2 = open_paramPage(browser)
    after_change = param_input2.get_attribute("value")
    assert after_change != before_change
    assert after_change == '111'
    param_input2.clear()
    param_input2.send_keys('222')
    time.sleep(2)
    # click 'OK' and cancel audit reason
    MainPage(browser).eleclick(browser.find_element_by_xpath("//span[text()=' OK ']/.."))
    assert MainPage(browser).is_element_showed("#audit-dialog") is True
    MainPage(browser).eleclick(browser.find_element_by_xpath("//span[text()='Cancel']/.."))
    # browser.find_element_by_xpath("//span[text()='Cancel']/..").click()
    # Will go back to the current Parameters Page and continue editing.
    assert 'parameters' in browser.current_url
    # click 'OK' and check the check box,then click 'ok'
    MainPage(browser).eleclick(browser.find_element_by_xpath("//span[text()=' OK ']/.."))
    time.sleep(3)
    browser.find_element_by_xpath("//*[@id='audit-dialog']/div/div[2]/mat-form-field/div/div/div/textarea").send_keys('for test')
    time.sleep(2)
    check_box = browser.find_element_by_xpath("//*[@id='audit-dialog']/div/div[2]/mat-checkbox/label/div/input")
    MainPage(browser).eleclick(check_box)
    time.sleep(3)
    # browser.find_element_by_xpath("////*[@id='audit-dialog']/div/div[2]/mat-checkbox/label/div/input").click()
    MainPage(browser).eleclick(browser.find_element_by_xpath("//span[text()='OK']/.."))
    time.sleep(2)
    param_input3 = open_paramPage(browser)
    param_input3.clear()
    param_input3.send_keys('333')
    time.sleep(2)
    # click 'OK' and audit reason dialog do not pop up
    MainPage(browser).eleclick(browser.find_element_by_xpath("//span[text()=' OK ']/.."))
    assert MainPage(browser).is_element_showed("#audit-dialog") is False
    time.sleep(3)
    assert 'process-order' in browser.current_url
    param_input4 = open_paramPage(browser)
    param_input4.clear()
    param_input4.send_keys('444')
    # click the order name
    browser.find_element_by_xpath("//a[@class='order-link']").click()
    # A dialog pops up to indicate whether stay this page or not
    assert MainPage(browser).is_element_showed("#error-message-dialog") is True
    # click 'Stay'
    browser.find_element_by_xpath("//*[@id='error-message-dialog']/div/div[3]/button[1]").click()
    assert 'parameters' in browser.current_url
    time.sleep(3)
    browser.find_element_by_xpath("//a[@class='order-link']").click()
    # click 'Leave'
    browser.find_element_by_xpath("//*[@id='error-message-dialog']/div/div[3]/button[2]").click()
    time.sleep(2)
    # the page will go to process order directly
    assert 'process-order' in browser.current_url


if __name__ == '__main__':
    pytest.main(["-s", "test_VS627922.py"])
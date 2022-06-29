# coding = utf-8
import time, re
from framework.basefunc import MainPage
import pytest

def test_ParaPage(browser):
    time.sleep(10)
    order_ele = browser.find_element_by_xpath("//div[contains(text(),'2BPLS')]")
    order_ele.click()
    time.sleep(3)
    # Check shows at the left top with order name, batch code
    order_info = browser.find_element_by_xpath("//a[@class='order-link']").get_attribute('textContent')
    assert '2BPLS/234565y' in order_info
    # make some changes
    phase_ele = browser.find_element_by_xpath("//button[@aria-label='Toggle PHASE57']")
    MainPage(browser).eleclick(phase_ele)
    browser.find_element_by_xpath("//span[contains(text(),'TEMP')]/../mat-form-field/div/div/div/input").clear()
    browser.find_element_by_xpath("//span[contains(text(),'TEMP')]/../mat-form-field/div/div/div/input").send_keys('66')
    time.sleep(2)
    # click the order name
    browser.find_element_by_xpath("//a[@class='order-link']").click()
    # A dialog pops up to indicate whether stay this page or not
    assert MainPage(browser).is_element_showed("#error-message-dialog") is True
    # click 'Leave'
    browser.find_element_by_xpath("//*[@id='error-message-dialog']/div/div[3]/button[2]").click()
    time.sleep(2)
    # the page will go to process order directly 
    assert 'process-order' in browser.current_url
    # go to paramter page from tracking page
    elementObj = browser.find_element_by_xpath("/html/body/app-root/div/app-navigation")
    browser.execute_script("arguments[0].className='show-nav'", elementObj)
    time.sleep(2)
    browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='tracking']").click()
    time.sleep(2)
    browser.find_element_by_xpath("//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/tbody/tr[1]/td[2]/div[1]/div").click()
    time.sleep(2)
    browser.find_element_by_xpath("//span[contains(text(),'TEMP')]/../mat-form-field/div/div/div/input").send_keys('66')
    time.sleep(2)
    # click the order name
    browser.find_element_by_xpath("//a[@class='order-link']").click()
    # A dialog pops up to indicate whether stay this page or not
    assert MainPage(browser).is_element_showed("#error-message-dialog") is True
    # click 'Leave'
    browser.find_element_by_xpath("//*[@id='error-message-dialog']/div/div[3]/button[2]").click()
    time.sleep(5)
    # the page will go to tracking page(Phase list)
    assert 'tracking' in browser.current_url


if __name__ == '__main__':
    pytest.main(["-s", "test_VS627837.py"])
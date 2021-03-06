# coding = utf-8
import time
from selenium.webdriver.common.keys import Keys
from framework.basefunc import MainPage
import pytest
def test_Footer(browser):
    time.sleep(4)
    order_ele = browser.find_element_by_xpath("//div[contains(text(),'FOR_GML')]/../..")
    order_ele.find_elements_by_tag_name("td")[-1].click()
    time.sleep(5)
    phase_ele1 = browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='phase_state_enabled']")
    phase_name1 = phase_ele1.find_element_by_xpath("./../../../../../../td[2]/div[1]/div").text
    MainPage(browser).eleclick(phase_ele1)
    time.sleep(5)
    # On execution page, execute a basic phase of an order, click blue 'OK' button
    browser.find_element_by_xpath("//*[@id='screen']/app-aebrs-footer/button").click()
    time.sleep(3)
    assert MainPage(browser).is_element_showed("mat-dialog-container") is True
    # click cancel
    cancel = browser.find_element_by_xpath("//button[@id='CHECK_LIST.cmpFooter.btnCancel']")
    MainPage(browser).eleclick(cancel)
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id='dialog']/div/div[3]/button[1]").click()
    time.sleep(5)
    assert 'tracking' in browser.current_url
    phase_ele2 = browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='phase_state_enabled']")
    phase_name2 = phase_ele2.find_element_by_xpath("./../../../../../../td[2]/div[1]/div").text
    assert phase_name1 == phase_name2
    # click enter
    MainPage(browser).eleclick(phase_ele2)
    time.sleep(5)
    Select_items = browser.find_elements_by_xpath("//*[@id='screen']/app-aebrs-table/form/table/tbody/tr/td[1]/div/div/input")
    for itme in Select_items:
        MainPage(browser).eleclick(itme)
    browser.find_element_by_xpath("//*[@id='screen']/app-aebrs-footer/button").click()
    time.sleep(5)
    # enter userId and password
    browser.find_element_by_xpath("//input[@id='CHECK_LIST.cmpFooter.txtUserId']").click()
    browser.find_element_by_xpath("//input[@id='CHECK_LIST.cmpFooter.txtUserId']").send_keys("corp\\qapart")
    browser.find_element_by_xpath("//input[@id='CHECK_LIST.cmpFooter.pwdSignature']").click()
    browser.find_element_by_xpath("//input[@id='CHECK_LIST.cmpFooter.pwdSignature']").send_keys("QQQaaa000")
    browser.find_element_by_xpath("//input[@id='CHECK_LIST.cmpFooter.pwdSignature']").send_keys(Keys.ENTER)
    time.sleep(10)
    assert 'tracking' in browser.current_url
    statuslist = browser.find_elements_by_xpath("//mat-icon")
    for status in statuslist:
        assert 'finished' in status.get_attribute('data-mat-icon-name') or 'planned' in status.get_attribute('data-mat-icon-name')

if __name__ == '__main__':
    pytest.main(["-s", "test_VS629827.py"])
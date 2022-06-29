# coding = utf-8
import time
import random
from framework.basefunc import MainPage
import pytest

def test_changeorder(browser):
    target = browser.find_element_by_xpath("//app-filter-box[@id='filterLOGIC_STATUS']/mat-icon")
    browser.execute_script("arguments[0].click();", target)
    time.sleep(2)
    # click selectAll
    select_all = browser.find_element_by_id("mat-checkbox-1-input")
    browser.execute_script("arguments[0].scrollIntoView();", select_all)
    MainPage(browser).eleclick(select_all)
    browser.find_element_by_xpath("/html/body/div[2]/div[1]").click()
    time.sleep(3)
    order_list = browser.find_elements_by_xpath("/html/body/app-root/div/div/app-process-order/div/div[2]/table/tbody/tr/td[2]/div[1]")
    order_datalist = []
    for order in order_list:
        order_data = order.get_attribute('textContent')
        order_datalist.append(order_data.strip('/'))
    # All the available orders will be displayed in the dropdown list
    time.sleep(3)
    track = browser.find_elements_by_css_selector("mat-icon[data-mat-icon-name='double_arrow']")
    MainPage(browser).eleclick(track[0])
    time.sleep(3)
    browser.find_element_by_xpath("//input[@aria-label='OrderName']").click()
    time.sleep(3)
    select_list = browser.find_elements_by_css_selector("span.mat-option-text")
    select_datalist = []
    for select in select_list:
        select_data = select.get_attribute('textContent')
        select_datalist.append(select_data.replace(" ", ""))
        assert select_data.replace(" ", "") in order_datalist
    # Click the order in the dropdown list to change the chosen order
    num = random.choice(range(len(select_datalist)))
    MainPage(browser).eleclick(select_list[num])
    browser.find_element_by_xpath("//*[@id='tracking-content']/app-tracking-list/div/div[2]").click()
    name = browser.find_element_by_xpath("//input[@aria-label='OrderName']").get_attribute('value')
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\test_VS591893.png")
    assert name == select_datalist[num]
    # Scroll on the dropdown list
    browser.find_element_by_xpath("//input[@aria-label='OrderName']").click()
    time.sleep(3)
    targetElem = browser.find_element_by_xpath("//*[contains(text(),'FROM_RPL')]")
    browser.execute_script("arguments[0].scrollIntoView();", targetElem)
    time.sleep(3)
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\focus.png")
    MainPage(browser).eleclick(targetElem)
    time.sleep(3)



if __name__ == '__main__':
    pytest.main(["-s", "test_VS591893.py"])
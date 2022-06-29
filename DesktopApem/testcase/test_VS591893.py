# coding = utf-8
import time
import random
from framework.common import Common
from selenium.webdriver.common.by import By
import pytest
def test_changeorder(browser):
    target = browser.find_element(By.XPATH, "//app-filter-box[@id='filterLOGIC_STATUS']/mat-icon")
    browser.execute_script("arguments[0].click();", target)
    time.sleep(2)
    # click selectAll
    browser.find_element(By.ID, "mat-checkbox-1").click()
    t_element = browser.find_element(By.XPATH, "/html/body/div[2]/div[1]")
    browser.execute_script("arguments[0].click();", t_element)
    time.sleep(3)
    order_list = browser.find_elements(By.XPATH, "/html/body/app-root/div/app-process-order/div/div[2]/table/tbody/tr/td[2]/div[1]")
    order_datalist = []
    for order in order_list:
        order_data = order.get_attribute('textContent')
        order_datalist.append(order_data.strip('/').replace(" ", ""))
    # All the available orders will be displayed in the dropdown list
    time.sleep(3)
    track = browser.find_elements(by=By.CSS_SELECTOR, value="mat-icon[data-mat-icon-name='double_arrow']")
    Common(browser).eleclick(track[0])
    time.sleep(3)
    browser.find_element(By.XPATH, "//input[@aria-label='OrderName']").click()
    time.sleep(3)
    select_list = browser.find_elements(by=By.CSS_SELECTOR, value="span.mat-option-text")
    select_datalist = []
    for select in select_list:
        select_data = select.get_attribute('textContent')
        select_datalist.append(select_data.replace(" ", ""))
        assert select_data.replace(" ", "") in order_datalist
    # Click the order in the dropdown list to change the chosen order
    num = random.choice(range(len(select_datalist)))
    Common(browser).eleclick(select_list[num])
    browser.find_element(By.XPATH, "//*[@id='tracking-content']/app-tracking-list/div/div[2]").click()
    name = browser.find_element(By.XPATH, "//input[@aria-label='OrderName']").get_attribute('value')
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\test_VS591893.png")
    assert name == select_datalist[num]
    # Scroll on the dropdown list
    browser.find_element(By.XPATH, "//input[@aria-label='OrderName']").click()
    time.sleep(3)
    targetElem = browser.find_element(By.XPATH, "//*[contains(text(),'FROM_RPL')]")
    browser.execute_script("arguments[0].scrollIntoView();", targetElem)
    time.sleep(3)
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\focus.png")
    Common(browser).eleclick(targetElem)
    time.sleep(3)



if __name__ == '__main__':
    pytest.main(["-s", "test_VS591893.py"])
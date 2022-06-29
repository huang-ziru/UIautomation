# coding = utf-8
import time
import random
from framework.basefunc import MainPage
import pytest

def test_IconStatus(browser):
    time.sleep(2)
    order_ele = browser.find_element_by_xpath("//div[contains(text(),'FROM_RPL')]/../..")
    order_ele.find_elements_by_tag_name("td")[-1].click()
    time.sleep(2)
    Status = browser.find_elements_by_css_selector("td[class ~= 'cdk-column-STATUS']")
    Exe_icon = browser.find_elements_by_css_selector("td[class ~= 'cdk-column-EXECUTION']")
    for i in range(len(Status)):
        phase_status = Status[i].get_attribute('textContent')
        icon_name = Exe_icon[i].find_element_by_tag_name("mat-icon").get_attribute('data-mat-icon-name')
        if phase_status == 'Ready':
            assert 'enabled' in icon_name
        elif phase_status == 'Not ready':
            assert 'planned' in icon_name
        else:
            assert phase_status.lower() in icon_name

    # consolidated mode
    elementObj = browser.find_element_by_xpath("/html/body/app-root/div/app-navigation")
    browser.execute_script("arguments[0].className='show-nav'", elementObj)
    time.sleep(2)
    browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='settings']").click()
    switch = browser.find_element_by_xpath("//div[@class='show-navigation'][5]/div/div[2]/mat-slide-toggle")
    if switch.find_element_by_tag_name('input').get_attribute('aria-checked') == 'false':
        MainPage(browser).eleclick(switch)
    time.sleep(5)
    browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='consolidated']").click()
    Con_Status = browser.find_elements_by_css_selector("td[class ~= 'cdk-column-STATUS']")
    Con_Exe_icon = browser.find_elements_by_css_selector("td[class ~= 'cdk-column-EXECUTION']")
    for j in range(len(Con_Status)):
        phase_status = Status[j].get_attribute('textContent')
        icon_name = Con_Exe_icon[j].find_element_by_tag_name("mat-icon").get_attribute('data-mat-icon-name')
        if phase_status == 'Ready':
            assert 'enabled' in icon_name
        elif phase_status == 'Not Ready':
            assert 'planned' in icon_name
        elif phase_status == 'Executing locally':
            assert 'executing' in icon_name
        else:
            assert phase_status.lower() in icon_name
    # restore data
    elementObj = browser.find_element_by_xpath("/html/body/app-root/div/app-navigation")
    browser.execute_script("arguments[0].className='show-nav'", elementObj)
    time.sleep(2)
    browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='settings']").click()
    switch = browser.find_element_by_xpath("//div[@class='show-navigation'][5]/div/div[2]/mat-slide-toggle")
    MainPage(browser).eleclick(switch)




if __name__ == '__main__':
    pytest.main(["-s", "test_VS626810.py"])
# coding = utf-8
import time

from selenium.webdriver import ActionChains
from framework.basefunc import MainPage
from framework.columsfunc import Func
import pytest

def test_columns(browser):
    elementObj = browser.find_element_by_xpath("/html/body/app-root/div/app-navigation")
    browser.execute_script("arguments[0].className='show-nav'", elementObj)
    time.sleep(2)
    browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='settings']").click()
    switch = browser.find_element_by_xpath("//div[@class='show-navigation'][5]/div/div[2]/mat-slide-toggle")
    if switch.find_element_by_tag_name('input').get_attribute('aria-checked') == 'true':
        MainPage(browser).eleclick(switch)
    time.sleep(5)
    browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='process_order']").click()
    track = browser.find_elements_by_css_selector("mat-icon[data-mat-icon-name='double_arrow']")
    MainPage(browser).eleclick(track[0])
    time.sleep(3)
    # it displays default setting(No., Phase, Status ,icon)
    default_head = browser.find_elements_by_xpath("//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/thead/tr/th")
    assert len(default_head) == 4
    for i in range(len(default_head)):
        head_name = default_head[i].find_element_by_xpath("div/div/div").get_attribute('textContent')
        assert head_name in ("No.", "Phase", "Status", "")
    browser.find_element_by_css_selector("mat-icon[data-mat-icon-name='visible_column']").click()
    all_list_option = browser.find_elements_by_xpath("//*[@id='colselectpanel']/mat-list-option")
    hide_list_option = browser.find_elements_by_css_selector("mat-list-option[class ~= 'hide']")
    for hide_option in hide_list_option:
        all_list_option.remove(hide_option)
    columns_list = []
    for list_option in all_list_option:
        option_text = list_option.find_element_by_css_selector("div.mat-list-text").get_attribute('textContent')
        columns_list.append("check" + option_text.strip())
    # Check default columns are not allowed to hide and are not in this list
        assert option_text not in ("No.", "Phase", "Status", "")
    # The related columns will show/hide in the order table
    time.sleep(2)
    back = browser.find_element_by_xpath("/html/body/div[2]/div[1]")
    MainPage(browser).eleclick(back)
    Func(browser).visiblecols(columns_list)
    for id in columns_list:
        headerid = "header" + id[5::]
        # Scroll to the location where the specified element appears
        target2 = browser.find_element_by_id(headerid)
        browser.execute_script("arguments[0].scrollIntoView();", target2)
        browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + id + ".png")
        assert id[5::] == browser.find_element_by_id(headerid).get_attribute('textContent')

def test_colums_Con(browser):
    # consolidation mode
    elementObj = browser.find_element_by_xpath("/html/body/app-root/div/app-navigation")
    browser.execute_script("arguments[0].className='show-nav'", elementObj)
    time.sleep(2)
    browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='settings']").click()
    switch = browser.find_element_by_xpath("//div[@class='show-navigation'][5]/div/div[2]/mat-slide-toggle")
    if switch.find_element_by_tag_name('input').get_attribute('aria-checked') == 'false':
           MainPage(browser).eleclick(switch)
    time.sleep(5)
    browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='consolidated']").click()
    browser.find_element_by_css_selector("mat-icon[data-mat-icon-name='visible_column']").click()
    time.sleep(5)
    all_list_option = browser.find_elements_by_xpath("//*[@id='colselectpanel']/mat-list-option")
    hide_list_option = browser.find_elements_by_css_selector("mat-list-option[class ~= 'hide']")
    for hide_option in hide_list_option:
        all_list_option.remove(hide_option)
    columns_list = []
    for list_option in all_list_option:
        option_text = list_option.find_element_by_css_selector("div.mat-list-text").get_attribute('textContent')
        columns_list.append("check" + option_text.strip())
    time.sleep(3)
    back = browser.find_element_by_xpath("/html/body/div[2]/div[1]")
    MainPage(browser).eleclick(back)
    Func(browser).visiblecols(columns_list)
    for id in columns_list:
        headerid = "header" + id[5::]
        # Scroll to the location where the specified element appears
        target2 = browser.find_element_by_id(headerid)
        browser.execute_script("arguments[0].scrollIntoView();", target2)
        browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + id + ".png")
        assert id[5::] == browser.find_element_by_id(headerid).get_attribute('textContent')
    # restore data
    browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='settings']").click()
    switch = browser.find_element_by_xpath("//div[@class='show-navigation'][5]/div/div[2]/mat-slide-toggle")
    MainPage(browser).eleclick(switch)
if __name__ == '__main__':
    pytest.main(["-s", "test_VS591862.py"])
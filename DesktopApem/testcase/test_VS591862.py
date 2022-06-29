# coding = utf-8
import time
from selenium.webdriver import ActionChains
from framework.common import Common
from framework.basefunc import MainPage
from framework.columsfunc import Func
from selenium.webdriver.common.by import By
import pytest
def test_columns(browser):
    time.sleep(3)
    track = browser.find_elements(by=By.CSS_SELECTOR, value="mat-icon[data-mat-icon-name='double_arrow']")
    Common(browser).eleclick(track[0])
    time.sleep(3)
    # hover on and show 'Visible Columns'
    mouse = browser.find_element(By.XPATH, "//*[@id='selectmenu']")
    ActionChains(browser).move_to_element(mouse).perform()
    hover_text = browser.find_element(By.XPATH, "/html/body/div[2]").text
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\visible_column(track).png")
    assert 'Visible Columns' == hover_text
    # check the visible columns list
    browser.find_element(By.CSS_SELECTOR, value="mat-icon[data-mat-icon-name='visible_column']").click()
    all_list_option = browser.find_elements(By.XPATH, "//*[@id='colselectpanel']/mat-list-option")
    hide_list_option = browser.find_elements(by=By.CSS_SELECTOR, value="mat-list-option[class ~= 'hide']")
    for hide_option in hide_list_option:
        all_list_option.remove(hide_option)
    columns_list = []
    for list_option in all_list_option:
        option_text = list_option.find_element(By.CSS_SELECTOR, value="div.mat-list-text").get_attribute('textContent')
        columns_list.append("check" + option_text.strip())
        # Check default columns are not allowed to hide and are not in this list
        assert option_text not in ("No.", "Phase", "Status")
    # The related columns will show/hide in the order table
    time.sleep(2)
    back = browser.find_element(By.XPATH, "/html/body/div[2]/div[1]")
    Common(browser).eleclick(back)
    Func(browser).visiblecols(columns_list)
    for id in columns_list:
        headerid = "header" + id[5::]
        # Scroll to the location where the specified element appears
        target2 = browser.find_element(By.ID, headerid)
        browser.execute_script("arguments[0].scrollIntoView();", target2)
        browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + id + ".png")
        assert id[5::] == browser.find_element(By.ID, headerid).get_attribute('textContent')
    # restore data
    Func(browser).cancelecols(columns_list)
    # it displays default setting(No., Phase, Status ,icon)
    default_head = browser.find_elements(By.XPATH, "//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/thead/tr/th")
    assert len(default_head) == 3
    for i in range(len(default_head)):
        if MainPage(default_head[i]).is_element_showed("div") is False:
            assert "".join(default_head[i].get_attribute('textContent').split()) == ""
        else:
            head_name = default_head[i].find_element(By.XPATH, "div/div/div").get_attribute('textContent')
            assert head_name in ("No.", "Phase", "Status")


def test_colums_Con(browser):
    # consolidation mode
    browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='settings']").click()
    switch = browser.find_element(By.XPATH, "//div[@class='show-navigation'][5]/div/div[2]/mat-slide-toggle")
    if switch.find_element(By.TAG_NAME, 'input').get_attribute('aria-checked') == 'false':
        Common(browser).eleclick(switch)
    time.sleep(5)
    browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='consolidated']").click()
    browser.find_element(By.CSS_SELECTOR, value="mat-icon[data-mat-icon-name='visible_column']").click()
    time.sleep(5)
    all_list_option = browser.find_elements(By.XPATH, "//*[@id='colselectpanel']/mat-list-option")
    hide_list_option = browser.find_elements(by=By.CSS_SELECTOR, value="mat-list-option[class ~= 'hide']")
    for hide_option in hide_list_option:
        all_list_option.remove(hide_option)
    columns_list = []
    for list_option in all_list_option:
        option_text = list_option.find_element(By.CSS_SELECTOR, value="div.mat-list-text").get_attribute('textContent')
        columns_list.append("check" + option_text.strip())
    time.sleep(3)
    back = browser.find_element(By.XPATH, "/html/body/div[2]/div[1]")
    Common(browser).eleclick(back)
    Func(browser).visiblecols(columns_list)
    for id in columns_list:
        headerid = "header" + id[5::]
        # print(headerid)
        # Scroll to the location where the specified element appears
        target2 = browser.find_element(By.ID, headerid)
        browser.execute_script("arguments[0].scrollIntoView();", target2)
        browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + id + ".png")
        assert id[5::] == browser.find_element(By.ID, headerid).get_attribute('textContent')
    # restore data
    # Func(browser).cancelecols(columns_list)
    browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='settings']").click()
    switch = browser.find_element(By.XPATH, "//div[@class='show-navigation'][5]/div/div[2]/mat-slide-toggle")
    Common(browser).eleclick(switch)

if __name__ == '__main__':
    pytest.main(["-s", "test_VS591862.py"])
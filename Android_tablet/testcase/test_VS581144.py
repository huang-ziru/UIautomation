# coding = utf-8
import datetime
from selenium import webdriver
import pytest
import time
import random
from framework.columsfunc import Func
from framework.columsfunc import testfilter
from framework.basefunc import MainPage
from selenium.webdriver.support.color import Color
import re
from selenium.webdriver.common.action_chains import ActionChains

# default status
# select "Planned", "Active", "Initiated", "Executing", "Cancelled by phase"
def test_defstatus(browser):
    table_tr_list = browser.find_elements_by_xpath("//div[@class='full show-navigation']/div[2]/table/tbody/tr")
    for tr in table_tr_list:
        table_td_list = tr.find_elements_by_tag_name("td")[1::]
        browser.get_screenshot_as_file(r"..\\report\\result_picture\\default_status.png")
        assert table_td_list[4].text in ("Planned", "Active", "Initiated", "Executing", "Cancelled by phase")
# select all status "Planned", "Active / Initiated", "Executing", "Cancelled by phase", "Cancelled", "Finished", "Archived", "Archived cancel", "Ext.Archived", "Ext.Archived cancel"
def test_Allstatus(browser):
    target = browser.find_element_by_xpath("//app-filter-box[@id='filterLOGIC_STATUS']/mat-icon")
    browser.execute_script("arguments[0].click();", target)
    time.sleep(2)
    # click selectAll
    select_all = browser.find_element_by_xpath("//mat-selection-list/section[1]/mat-checkbox/label/div/input")
    browser.execute_script("arguments[0].click();", select_all)
    browser.find_element_by_xpath("/html/body/div[2]/div[1]").click()
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\selectall_status.png")
    time.sleep(2)
    table_tr_list = browser.find_elements_by_xpath("//div[@class='full show-navigation']/div[2]/table/tbody/tr")
    for tr in table_tr_list:
        table_td_list = tr.find_elements_by_tag_name("td")[1::]
        # print(table_td_list[4])
        assert table_td_list[4].text in ("Planned", "Active", "Initiated", "Executing", "Cancelled by phase", "Cancelled", "Finished", "Archived", "Archived cancel", "Ext.Archived", "Ext.Archived cancel")

def test_color(browser):
    Func(browser).clear_Status()
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\color.png")
    table_tr_list = browser.find_elements_by_xpath("//div[@class='full show-navigation']/div[2]/table/tbody/tr")
    for i in range(len(table_tr_list)):
        backcolor = table_tr_list[i].value_of_css_property('background-color')
        assert Color.from_string(backcolor) == Color.from_string('#ffffff')
# height line
def test_tr_height(browser):
    table_tr_list = browser.find_elements_by_xpath("//div[@class='full show-navigation']/div[2]/table/tbody/tr")
    for i in range(len(table_tr_list)):
        count = i + 1
        td = table_tr_list[i]
        div_list = td.find_element_by_css_selector("td[class ~= 'order-column']").find_elements_by_tag_name("div")
        tr_path = "//tbody/tr[" + str(count) + "]"
        height_before = []
        for divv1 in div_list:
            height_before.append(divv1.value_of_css_property('max-height'))
        height_after = []
        browser.find_element_by_xpath(tr_path).click()
        time.sleep(3)
        for divv2 in div_list:
            height_after.append(divv2.value_of_css_property('max-height'))
        # print("after", height_after)
        if 'none' not in height_after:
            assert height_after[0] == '500px'
            assert height_after[1] == '500px'
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\tr_height.png")

# Circle function
def test_Circle(browser):
    Func(browser).clear_Status()
    table_tr_list = browser.find_elements_by_xpath("//div[@class='full show-navigation']/div[2]/table/tbody/tr")
    for i in range(len(table_tr_list)):
        td = table_tr_list[i]
        circle_ele = td.find_element_by_css_selector("circle[class='ng-star-inserted']")
        p_text = td.find_element_by_css_selector("div[class='back-circle']>p").text
        #Percentage of the display on the circle
        offset = float(circle_ele.value_of_css_property('stroke-dashoffset')[:-2])
        array = float(circle_ele.value_of_css_property('stroke-dasharray')[:-2])
        exe_progress = re.findall(r'\d+', p_text)
        if offset == array:
            assert exe_progress[0] == '0'
        elif offset == 0.0:
            assert exe_progress[0] == exe_progress[1]
        else:
            progress_circle = round((offset / array), 3)
            progress = round((float(exe_progress[0]) / float(exe_progress[1])), 3)
            #The absolute difference is less than 0.005
            assert abs(progress_circle - progress) <= 0.005
# hover on 》
def test_hovertrack(browser):
    target = browser.find_element_by_xpath("/html/body/app-root/div/div/app-process-order/div/div[2]/table/tbody/tr[1]/td[8]/a/mat-icon")
    browser.execute_script("arguments[0].click();", target)
    time.sleep(5)
    assert 'tracking' in browser.current_url
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\hovertrack.png")

# filter show all orders name
def test_All(browser):
    Func(browser).clear_Status()
    target = browser.find_element_by_xpath("/html/body/app-root/div/div/app-process-order/div/div[2]/table/thead/tr/th[2]")
    mat_option = testfilter(browser).test_selectAll(target)
    table_data = MainPage(browser).get_table()
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\order_selectall.png")
    assert len(mat_option) == len(table_data)

# filter cancel selectAll
def test_clear(browser):
    Func(browser).clear_Status()
    target = browser.find_element_by_xpath("/html/body/app-root/div/div/app-process-order/div/div[2]/table/thead/tr/th[2]")
    mat_option = testfilter(browser).test_selectclear(target)
    table_data = MainPage(browser).get_table()
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\order_clear.png")
    assert len(table_data) == 0
    assert len(mat_option) == 0

# Randomly select a piece of data
def test_randomselect(browser):
    Func(browser).clear_Status()
    target = browser.find_element_by_xpath("//app-filter-box[@id='filterCODE']")
    select_list = testfilter(browser).test_selectone(target)
    num = random.choice(range(len(select_list)))
    check_data = select_list[num]
    #get the order name which is selected
    order_name = check_data.find_elements_by_tag_name("div")[2].text
    browser.execute_script("arguments[0].click();", check_data)
    back = browser.find_element_by_xpath("/html/body/div[2]/div[1]")
    browser.execute_script("arguments[0].click();", back)
    time.sleep(2)
    td = browser.find_elements_by_xpath("/html/body/app-root/div/div/app-process-order/div/div[2]/table/tbody/tr/td[2]")
    order_td = MainPage(browser).td_data(td)
    order_list_name = MainPage(browser).table_ordername(order_td)
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\order_selectone.png")
    assert len(order_td) == 1
    #assert the table shows the selected data
    assert order_name == order_list_name[0]

# add select a data and show it
def test_add(browser):
    Func(browser).clear_Status()
    order_name = []
    target1 = browser.find_element_by_xpath("//app-filter-box[@id='filterCODE']")
    select_list1 = testfilter(browser).test_selectone(target1)
    check_data1 = select_list1[0]
    #select one
    order_name.append(check_data1.find_elements_by_tag_name("div")[2].text)
    browser.execute_script("arguments[0].click();", check_data1)
    time.sleep(2)
    back = browser.find_element_by_xpath("/html/body/div[2]/div[1]")
    browser.execute_script("arguments[0].click();", back)
    time.sleep(2)
    #add select another data which is not be selected and get the text
    target2 = browser.find_element_by_xpath("//app-filter-box[@id='filterCODE']/mat-icon")
    browser.execute_script("arguments[0].click();", target2)
    select_list = browser.find_elements_by_xpath("//div[@class='ng-star-inserted']/mat-list-option")
    #check if be selected
    for select in select_list:
        if select.get_attribute('aria-selected') == 'false':
            order_name.append(select.find_elements_by_tag_name("div")[2].text)
            select.click()
            break
    time.sleep(3)
    back = browser.find_element_by_xpath("/html/body/div[2]/div[1]")
    browser.execute_script("arguments[0].click();", back)
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\order_add.png")
    time.sleep(2)
    td = browser.find_elements_by_xpath("/html/body/app-root/div/div/app-process-order/div/div[2]/table/tbody/tr/td[2]")
    order_td = MainPage(browser).td_data(td)
    order_list_name = MainPage(browser).table_ordername(order_td)
    #assert table data equal selected data
    for i in range(len(order_list_name)):
        assert order_name[i] == order_list_name[i]

# cancle select a data and verify the data is not in table
def test_cancel(browser):
    Func(browser).clear_Status()
    global order_name
    target2 = browser.find_element_by_xpath("//app-filter-box[@id='filterCODE']/mat-icon")
    browser.execute_script("arguments[0].click();", target2)
    select_list = browser.find_elements_by_xpath("//div[@class='ng-star-inserted']/mat-list-option")
    for ele in select_list:
        if ele.get_attribute('aria-selected') == 'true':
            order_name = ele.find_elements_by_tag_name("div")[2].text
            ele.click()
        break
    time.sleep(2)
    back = browser.find_element_by_xpath("/html/body/div[2]/div[1]")
    browser.execute_script("arguments[0].click();", back)
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\order_cancel.png")
    time.sleep(3)
    td = browser.find_elements_by_xpath("/html/body/app-root/div/div/app-process-order/div/div[2]/table/tbody/tr/td[2]")
    order_td = MainPage(browser).td_data(td)
    order_list_name = MainPage(browser).table_ordername(order_td)
    assert order_name not in order_list_name

# the search in filter box
def test_search(browser):
    Func(browser).clear_Status()
    target = browser.find_element_by_xpath("//app-filter-box[@id='filterCODE']")
    #search with key word 'order'
    select_dic = testfilter(browser).test_filtersearch(target, 'order')
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\order_searchdata.png")
    #There is matching data and case insensitive
    for selectorder in select_dic['search_list']:
        searchresult = re.findall(r'order', selectorder, re.I)
        assert len(searchresult) != 0
    #there is not matching data in hide datas
    for noselect in select_dic['no_search_list']:
        noresult =  re.findall(r'order', noselect, re.I)
        assert len(noresult) == 0
    back = browser.find_element_by_xpath("/html/body/div[2]/div[1]")
    browser.execute_script("arguments[0].click();", back)
#
#search for none matching data
def test_search_none(browser):
    Func(browser).clear_Status()
    target1 = browser.find_element_by_xpath("//app-filter-box[@id='filterCODE']")
    target = browser.find_element_by_xpath("//app-filter-box[@id='filterCODE']")
    select_dic = testfilter(browser).test_filtersearch(target, '456')
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\order_searchnone.png")
    for selectorder in select_dic['search_list']:
        searchresult = re.findall(r'456', selectorder, re.I)
        assert len(searchresult) == 0
    for noselect in select_dic['no_search_list']:
        noresult = re.findall(r'456', noselect, re.I)
        assert len(noresult) == 0
    back = browser.find_element_by_xpath("/html/body/div[2]/div[1]")
    browser.execute_script("arguments[0].click();", back)

# search data and selct one data,then check the box'Add current selection to filter'
def test_checkadd(browser):
    Func(browser).clear_Status()
    target = browser.find_element_by_xpath("//app-filter-box[@id='filterCODE']")
    browser.execute_script("arguments[0].click();", target.find_element_by_tag_name("mat-icon"))
    select_all = browser.find_element_by_xpath("//*[@id='filcheck']/section[1]/mat-checkbox")
    if select_all.find_element_by_tag_name("input").get_attribute('aria-checked') == 'true':
        select_all.click()
        # select one data that name is 'FROM_RPL'
    browser.find_element_by_xpath("//div[text()=' FROM_RPL ']/../..").click()
    time.sleep(3)
    back = browser.find_element_by_xpath("/html/body/div[2]/div[1]")
    browser.execute_script("arguments[0].click();", back)
    time.sleep(3)
    select_dic = testfilter(browser).test_filtersearch(target, 'order')
    visual = select_dic['visual_list']
    num = random.choice(range(len(visual)))
    visual[num].click()
    browser.find_element_by_xpath("//*[@id='filcheck']/section[2]/mat-checkbox/label").click()
    time.sleep(3)
    back = browser.find_element_by_xpath("/html/body/div[2]/div[1]")
    browser.execute_script("arguments[0].click();", back)
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\order_checkadd.png")
    td = browser.find_elements_by_xpath("/html/body/app-root/div/div/app-process-order/div/div[2]/table/tbody/tr/td[2]")
    order_td = MainPage(browser).td_data(td)
    order_list_name = MainPage(browser).table_ordername(order_td)
    assert "FROM_RPL" == order_list_name[0]
    assert "order".upper() in order_list_name[1].upper()
    assert len(order_td) == 2

# search data and selct one data,but do not check the box'Add current selection to filter'
def test_checknull(browser):
    Func(browser).clear_Status()
    target = browser.find_element_by_xpath("//app-filter-box[@id='filterCODE']")
    browser.execute_script("arguments[0].click();", target.find_element_by_tag_name("mat-icon"))
    select_all = browser.find_element_by_xpath("//*[@id='filcheck']/section[1]/mat-checkbox")
    if select_all.find_element_by_tag_name("input").get_attribute('aria-checked') == 'true':
        select_all.click()
    browser.find_element_by_xpath("//div[text()=' FROM_RPL ']/../..").click()
    time.sleep(3)
    back = browser.find_element_by_xpath("/html/body/div[2]/div[1]")
    browser.execute_script("arguments[0].click();", back)
    time.sleep(3)
    select_dic = testfilter(browser).test_filtersearch(target, 'order')
    visual = select_dic['visual_list']
    num = random.choice(range(len(visual)))
    visual[num].click()
    time.sleep(3)
    back = browser.find_element_by_xpath("/html/body/div[2]/div[1]")
    browser.execute_script("arguments[0].click();", back)
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\order_checknull.png")
    td = browser.find_elements_by_xpath("/html/body/app-root/div/div/app-process-order/div/div[2]/table/tbody/tr/td[2]")
    order_td = MainPage(browser).td_data(td)
    order_list_name = MainPage(browser).table_ordername(order_td)
    assert len(order_td) == 1
    assert "order".upper() in order_list_name[0].upper()

if __name__ == '__main__':
    pytest.main(["-s", "test_VS581144.py"])


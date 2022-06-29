# coding = utf-8
import time
import random, re
from framework.basefunc import MainPage
from framework.columsfunc import Func
from framework.columsfunc import testfilter
import pytest

class TesttrackFilter():
    def prepare(self, browser):
        track = browser.find_elements_by_css_selector("mat-icon[data-mat-icon-name='double_arrow']")
        MainPage(browser).eleclick(track[3])
        time.sleep(3)
        columns_list = ['checkAuto.', 'checkAssigned WkSt.', 'checkUser Status', 'checkExecuting WkSt.','checkExecuting User', 'checkRepetition Count', 'checkUser RUDO', 'checkWkSt. RUDO']
        Func(browser).visiblecols(columns_list)
    def test_filtertrack_number(self, browser):
        TesttrackFilter.prepare(self, browser)
        table_head_list = MainPage(browser).get_tablehead()
        for l in range(len(table_head_list)):
            head_name = table_head_list[l].find_elements_by_tag_name('div')[2].text
            if head_name in ('No.', 'Repetition Count'):
                headid = "header" + head_name
                target1 = browser.find_element_by_id(headid)
                browser.execute_script("arguments[0].scrollIntoView();", target1)
                target = table_head_list[l].find_element_by_tag_name("mat-icon")
                browser.execute_script("arguments[0].click();", target)
                time.sleep(2)
                # input the min number and max number,also '1'and '2' can be modified
                browser.find_element_by_xpath("//input[@formindex='1']").send_keys('2')
                time.sleep(3)
                target2 = browser.find_element_by_xpath("//input[@formindex='2']")
                browser.execute_script("arguments[0].click();", target2)
                browser.find_element_by_xpath("//input[@formindex='2']").send_keys('4')
                browser.find_element_by_xpath("/html/body/div[2]").click()
                browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + head_name + ".png")
                td_path = "//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/tbody/tr/td[" + str(l + 2) + "]"
                td_list = browser.find_elements_by_xpath(td_path)
                td_data = MainPage(browser).td_data(td_list)
                try:
                    if td_data != ['']:
                        for num_p in td_data:
                            assert num_p >= '1' and num_p <= '2'
                finally:
                    MainPage(browser).clear_input(table_head_list[l], "//input[@formindex='1']", "//input[@formindex='2']")
    def test_selectall(self, browser):
        TesttrackFilter.prepare(self, browser)
        table_head_list = MainPage(browser).get_tablehead()
        for l in range(len(table_head_list)):
            head_name = table_head_list[l].find_elements_by_tag_name('div')[2].text
            #except the status column and the columns which type is date or number
            if head_name not in ('No.', 'Repetition Count'):
                headid = "header" + head_name
                target = browser.find_element_by_id(headid)
                browser.execute_script("arguments[0].scrollIntoView();", target)
                time.sleep(5)
                mat_text = testfilter(browser).test_selectAll(table_head_list[l])
                # browser.find_element_by_xpath("/html/body/div[2]/div[1]").click()
                td_path = "//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/tbody/tr/td[" + str(l + 2) + "]"
                td_list = browser.find_elements_by_xpath(td_path)
                td_data = MainPage(browser).td_data(td_list)
                browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + head_name + "_all.png")
                #the column's data is null
                for data in td_data:
                    if data == '':
                        assert '(Blank)' in mat_text
                    else:
                        assert data in mat_text
                time.sleep(2)

    def test_filterclear(self, browser):
        TesttrackFilter.prepare(self, browser)
        table_head_list = MainPage(browser).get_tablehead()
        for l in range(len(table_head_list)):
            head_name = table_head_list[l].find_elements_by_tag_name('div')[2].text
            if head_name not in ('No.', 'Repetition Count'):
                headid = "header" + head_name
                target = browser.find_element_by_id(headid)
                browser.execute_script("arguments[0].scrollIntoView();", target)
                time.sleep(3)
                # print(head_name)
                mat_list = testfilter(browser).test_selectclear(table_head_list[l])
                browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + head_name + "_clear.png")
                td_path = "//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/tbody/tr/td[" + str(l + 2) + "]"
                td_list = browser.find_elements_by_xpath(td_path)
                td_data = MainPage(browser).td_data(td_list)
                assert td_data == ['']
                table_head_list[l].find_element_by_tag_name("mat-icon").click()
                browser.find_element_by_xpath("//*[@id='filcheck']/section[1]/mat-checkbox").click()
                time.sleep(2)
                target = browser.find_element_by_xpath("/html/body/div[2]/div[1]")
                browser.execute_script("arguments[0].click();", target)


    def test_filterrandom(self, browser):
        TesttrackFilter.prepare(self, browser)
        table_head_list = MainPage(browser).get_tablehead()
        for l in range(len(table_head_list)):
            head_name = table_head_list[l].find_elements_by_tag_name('div')[2].text
            if head_name not in ('No.', 'Repetition Count'):
                headid = "header" + head_name
                target = browser.find_element_by_id(headid)
                browser.execute_script("arguments[0].scrollIntoView();", target)
                time.sleep(3)
                mat_list = testfilter(browser).test_selectone(table_head_list[l])
                num = random.choice(range(len(mat_list)))
                check_data = mat_list[num]
                mat_text = check_data.find_elements_by_tag_name("div")[2].text
                browser.execute_script("arguments[0].click();", check_data)
                target = browser.find_element_by_xpath("/html/body/div[2]/div[1]")
                browser.execute_script("arguments[0].click();", target)
                time.sleep(2)
                browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + head_name + "_selectone.png")
                td_path = "//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/tbody/tr/td[" + str(l + 2) + "]"
                td_list = browser.find_elements_by_xpath(td_path)
                td_data = MainPage(browser).td_data(td_list)
                if len(mat_list) == 1 and mat_text == '(Blank)':
                    # 7 is the total number of table data
                    assert len(td_data) == 11
                else:
                    for data in td_data:
                        if data == '':
                            assert mat_text == '(Blank)'
                        else:
                            assert mat_text == data
                mat_pass = testfilter(browser).test_selectAll(table_head_list[l])

 # cancle selected data
    def test_cancel(self, browser):
        global mat_text
        TesttrackFilter.prepare(self, browser)
        table_head_list = MainPage(browser).get_tablehead()
        for l in range(len(table_head_list)):
            head_name = table_head_list[l].find_elements_by_tag_name('div')[2].text
            if head_name not in ('No.', 'Repetition Count'):
                headid = "header" + head_name
                target = browser.find_element_by_id(headid)
                browser.execute_script("arguments[0].scrollIntoView();", target)
                time.sleep(3)
                target2 = table_head_list[l].find_element_by_tag_name("mat-icon")
                browser.execute_script("arguments[0].click();", target2)
                time.sleep(3)
                #get the text showed in filter
                select_list = browser.find_elements_by_xpath("//div[@class='ng-star-inserted']/mat-list-option")
                select_text = select_list[0].find_elements_by_tag_name("div")[2].text
                #cancel a data that is selected
                for ele in select_list:
                    if ele.get_attribute('aria-selected') == 'true':
                        mat_text = ele.find_elements_by_tag_name("div")[2].text
                        ele.click()
                    break
                time.sleep(2)
                target = browser.find_element_by_xpath("/html/body/div[2]/div[1]")
                browser.execute_script("arguments[0].click();", target)
                time.sleep(2)
                browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + head_name + "_cancel.png")
                time.sleep(3)
                td_path = "//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/tbody/tr/td[" + str(l + 2) + "]"
                td_list = browser.find_elements_by_xpath(td_path)
                td_data = MainPage(browser).td_data(td_list)
                # if the column data is null
                if len(select_list) == 1 and select_text == '(Blank)':
                    assert td_data == ['']
                else:
                    for data in td_data:
                        assert mat_text != data
                mat_pass = testfilter(browser).test_selectAll(table_head_list[l])

    def test_search(self, browser):
        TesttrackFilter.prepare(self, browser)
        table_head_list = MainPage(browser).get_tablehead()
        for l in range(len(table_head_list)):
            head_name = table_head_list[l].find_elements_by_tag_name('div')[2].text
            if head_name not in ('No.', 'Repetition Count'):
                headid = "header" + head_name
                target = browser.find_element_by_id(headid)
                browser.execute_script("arguments[0].scrollIntoView();", target)
                time.sleep(3)
                target2 = table_head_list[l].find_element_by_tag_name("mat-icon")
                browser.execute_script("arguments[0].click();", target2)
                time.sleep(3)
                select_dic = testfilter(browser).test_filtersearch(table_head_list[l], 'ac')
                browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + head_name + "_search.png")
                time.sleep(2)
                for selectorder in select_dic['search_list']:
                    searchresult = re.findall(r'ac', selectorder, re.I)
                    assert len(searchresult) != 0
                for noselect in select_dic['no_search_list']:
                    noresult = re.findall(r'ac', noselect, re.I)
                    assert len(noresult) == 0
                target = browser.find_element_by_xpath("/html/body/div[2]/div[1]")
                browser.execute_script("arguments[0].click();", target)
                mat_pass = testfilter(browser).test_selectAll(table_head_list[l])




if __name__ == '__main__':
    pytest.main(["-s", "test_VS591875.py"])
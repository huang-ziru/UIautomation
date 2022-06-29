# coding = utf-8
import time
import pytest
import re, random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from framework.common import Common
from framework.baseFunc_table import func_for_table
from framework.Login import prepare
from selenium.webdriver.common.by import By

class Test_filter():
    # test the filter which it's type is date
    def test_datefilter(self, browser):
        prepare(browser).login_after()
        table_head_list = Common(browser).get_tablehead()
        for l in range(len(table_head_list)):
            #get the column head name
            head_name = table_head_list[l].find_elements(By.TAG_NAME, 'div')[2].text
            if head_name in ('Date', 'End Date'):
                td_path = "/html/body/app-root/div/app-process-order/div/div[2]/table/tbody/tr/td[" + str(l + 2) + "]"
                td_list = browser.find_elements(By.XPATH, td_path)
                td_data_bef = Common(browser).td_data(td_list)
                target = table_head_list[l].find_element(By.TAG_NAME, "mat-icon")
                browser.execute_script("arguments[0].click();", target)
                # input a valid date range ('3/12/2020'and '4/12/2020' can be modified )
                browser.find_element(By.XPATH, "//input[@placeholder='Start date']").click()
                browser.find_element(By.XPATH, "//input[@placeholder='Start date']").send_keys('3/12/2020')
                time.sleep(2)
                browser.find_element(By.XPATH, "//input[@placeholder='End date']").click()
                browser.find_element(By.XPATH, "//input[@placeholder='End date']").send_keys('4/12/2020')
                browser.find_element(By.XPATH, "//input[@placeholder='End date']").send_keys(Keys.ENTER)
                body_element=browser.find_element(By.XPATH, "/html/body/div[2]")
                browser.execute_script("arguments[0].click();", body_element)
                # browser.find_element(By.XPATH, "/html/body/div[2]").click()
                browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + head_name + ".png")
                td_path = "/html/body/app-root/div/app-process-order/div/div[2]/table/tbody/tr/td[" + str(l + 2) + "]"
                td_list = browser.find_elements(By.XPATH, td_path)
                # get the date datas of table
                td_data = Common(browser).td_data(td_list)
                try:
                    # There is data in the date range
                    if td_data != ['']:
                        for str_p in td_data:
                            dateTime_p = Common(browser).datetime_str(str_p)
                            assert dateTime_p >= Common(browser).datetime_str('3/12/2020') and dateTime_p <= Common(browser).datetime_str('4/12/2020')
                    else:
                        # There is not data in the date range
                        for date in td_data_bef:
                            if date != '':
                                dateTime_p = Common(browser).datetime_str(date)
                                assert dateTime_p < Common(browser).datetime_str('3/12/2020') or dateTime_p > Common(browser).datetime_str('4/12/2020')
                finally:
                    # clear the input
                    func_for_table(browser).clear_input(table_head_list[l], "//input[@placeholder='Start date']", "//input[@placeholder='End date']")
    #test the filter which it's type is number
    def test_numberfilter(self, browser):
        prepare(browser).login_after()
        table_head_list = Common(browser).get_tablehead()
        for l in range(len(table_head_list)):
            head_name = table_head_list[l].find_elements(By.TAG_NAME, 'div')[2].text
            if head_name in ('Rep.', 'Ver.', 'Quantity'):
                headid = "header" + head_name
                target1 = browser.find_element(By.ID, headid)
                browser.execute_script("arguments[0].scrollIntoView();", target1)
                target = table_head_list[l].find_element(By.TAG_NAME, "mat-icon")
                browser.execute_script("arguments[0].click();", target)
                time.sleep(2)
                #input the min number and max number,also '1'and '2' can be modified
                browser.find_element(By.XPATH, "//input[@formindex='1']").send_keys('1')
                time.sleep(3)
                target2 = browser.find_element(By.XPATH, "//input[@formindex='2']")
                browser.execute_script("arguments[0].click();", target2)
                browser.find_element(By.XPATH, "//input[@formindex='2']").send_keys('2')
                # browser.find_element(By.XPATH, "/html/body/div[2]").click()
                body_element = browser.find_element(By.XPATH, "/html/body/div[2]")
                browser.execute_script("arguments[0].click();", body_element)
                browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + head_name + ".png")
                td_path = "/html/body/app-root/div/app-process-order/div/div[2]/table/tbody/tr/td[" + str(l + 2) + "]"
                td_list = browser.find_elements(By.XPATH, td_path)
                td_data = Common(browser).td_data(td_list)
                try:
                    if td_data != ['']:
                        for num_p in td_data:
                            assert num_p >= '1' and num_p <= '2'
                finally:
                    func_for_table(browser).clear_input(table_head_list[l], "//input[@formindex='1']", "//input[@formindex='2']")
# #test the filter which it's type is text
class Testtextfilter():
    def test_selectall(self, browser):
        prepare(browser).login_after()
        table_head_list = Common(browser).get_tablehead()
        for l in range(1, len(table_head_list)):
            head_name = table_head_list[l].find_elements(By.TAG_NAME, 'div')[2].text
            #except the status column and the columns which type is date or number
            if head_name not in ('Rep.', 'Ver.', 'Quantity', 'Date', 'End Date', 'Status'):
                #PO column's text in html is 'PO '
                if head_name == 'PO':
                    headid = "header" + head_name + " "
                else:
                    headid = "header" + head_name
                target = browser.find_element(By.ID, headid)
                browser.execute_script("arguments[0].scrollIntoView();", target)
                time.sleep(5)
                mat_text = func_for_table(browser).test_selectAll(table_head_list[l])
                td_path = "/html/body/app-root/div/app-process-order/div/div[2]/table/tbody/tr/td[" + str(l + 2) + "]"
                td_list = browser.find_elements(By.XPATH, td_path)
                td_data = Common(browser).td_data(td_list)
                browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + head_name + "_all.png")
                #the column's data is null
                for data in td_data:
                    if data == '':
                        assert '(Blank)' in mat_text
                    else:
                        assert data in mat_text
                time.sleep(2)

    def test_filterclear(self,browser):
        prepare(browser).login_after()
        table_head_list = Common(browser).get_tablehead()
        for l in range(1, len(table_head_list)):
            head_name = table_head_list[l].find_elements(By.TAG_NAME, 'div')[2].text
            if head_name not in ('Rep.', 'Ver.', 'Quantity', 'Date', 'End Date', 'Status'):
                if head_name == 'PO':
                    headid = "header" + head_name + " "
                else:
                    headid = "header" + head_name
                target = browser.find_element(By.ID, headid)
                browser.execute_script("arguments[0].scrollIntoView();", target)
                time.sleep(3)
                # print(head_name)
                mat_list = func_for_table(browser).test_selectclear(table_head_list[l])
                browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + head_name + "_clear.png")
                target = browser.find_element(By.XPATH, "/html/body/div[2]/div[1]")
                browser.execute_script("arguments[0].click();", target)
                td_path = "/html/body/app-root/div/app-process-order/div/div[2]/table/tbody/tr/td[" + str(l + 2) + "]"
                td_list = browser.find_elements(By.XPATH, td_path)
                td_data = Common(browser).td_data(td_list)
                assert td_data == ['']
                table_head_list[l].find_element(By.TAG_NAME, "mat-icon").click()
                browser.find_element(By.XPATH, "//*[@id='filcheck']/section[1]/mat-checkbox").click()
                time.sleep(2)
                target2 = browser.find_element(By.XPATH, "/html/body/div[2]/div[1]")
                browser.execute_script("arguments[0].click();", target2)

#
    def test_filterrandom(self, browser):
        prepare(browser).login_after()
        table_head_list = Common(browser).get_tablehead()
        for l in range(1, len(table_head_list)):
            head_name = table_head_list[l].find_elements(By.TAG_NAME, 'div')[2].text
            if head_name not in ('Rep.', 'Ver.', 'Quantity', 'Date', 'End Date', 'Status'):
                if head_name == 'PO':
                    headid = "header" + head_name + " "
                else:
                    headid = "header" + head_name
                target = browser.find_element(By.ID, headid)
                browser.execute_script("arguments[0].scrollIntoView();", target)
                time.sleep(3)
                mat_list = func_for_table(browser).test_selectone(table_head_list[l])
                num = random.choice(range(len(mat_list)))
                check_data = mat_list[num]
                mat_text = check_data.find_elements(By.TAG_NAME, "div")[2].text
                browser.execute_script("arguments[0].click();", check_data)
                target = browser.find_element(By.XPATH, "/html/body/div[2]/div[1]")
                browser.execute_script("arguments[0].click();", target)
                time.sleep(2)
                browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + head_name + "_selectone.png")
                td_path = "/html/body/app-root/div/app-process-order/div/div[2]/table/tbody/tr/td[" + str(l + 2) + "]"
                td_list = browser.find_elements(By.XPATH, td_path)
                td_data = Common(browser).td_data(td_list)
                if len(mat_list) == 1 and mat_text == '(Blank)':
                    # 7 is the total number of table data
                    assert len(td_data) == 5
                else:
                    for data in td_data:
                        if data == '':
                            assert mat_text == '(Blank)'
                        else:
                            assert mat_text == data
                mat_pass = func_for_table(browser).test_selectAll(table_head_list[l])

 # cancle selected data
    def test_cancel(self, browser):
        prepare(browser).login_after()
        global mat_text
        table_head_list = Common(browser).get_tablehead()
        for l in range(1, len(table_head_list)):
            head_name = table_head_list[l].find_elements(By.TAG_NAME, 'div')[2].text
            if head_name not in ('Rep.', 'Ver.', 'Quantity', 'Date', 'End Date', 'Status'):
                if head_name == 'PO':
                    headname = head_name + " "
                else:
                    headname = head_name
                headid = "header" + headname
                target = browser.find_element(By.ID, headid)
                browser.execute_script("arguments[0].scrollIntoView();", target)
                time.sleep(3)
                target2 = table_head_list[l].find_element(By.TAG_NAME, "mat-icon")
                browser.execute_script("arguments[0].click();", target2)
                time.sleep(3)
                #get the text showed in filter
                select_list = browser.find_elements(By.XPATH, "//div[@class='ng-star-inserted']/mat-list-option")
                select_text = select_list[0].find_elements(By.TAG_NAME, "div")[2].text
                #cancel a data that is selected
                for ele in select_list:
                    if ele.get_attribute('aria-selected') == 'true':
                        mat_text = ele.find_elements(By.TAG_NAME, "div")[2].text
                        ele.click()
                    break
                time.sleep(2)
                target = browser.find_element(By.XPATH, "/html/body/div[2]/div[1]")
                browser.execute_script("arguments[0].click();", target)
                time.sleep(2)
                browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + head_name + "_cancel.png")
                time.sleep(3)
                td_path = "/html/body/app-root/div/app-process-order/div/div[2]/table/tbody/tr/td[" + str(l + 2) + "]"
                td_list = browser.find_elements(By.XPATH, td_path)
                td_data = Common(browser).td_data(td_list)
                # if the column data is null
                if len(select_list) == 1 and select_text == '(Blank)':
                    assert td_data == ['']
                else:
                    for data in td_data:
                        assert mat_text != data
                mat_pass = func_for_table(browser).test_selectAll(table_head_list[l])
 #
 #     # there is a defect here,so comment it out
    def test_search(self,browser):
        prepare(browser).login_after()
        table_head_list = Common(browser).get_tablehead()
        for l in range(1, len(table_head_list)):
            head_name = table_head_list[l].find_elements(By.TAG_NAME, 'div')[2].text
            if head_name not in ('Rep.', 'Ver.', 'Quantity', 'Date', 'End Date', 'Status'):
                if head_name == 'PO':
                     headname = head_name + " "
                else:
                    headname = head_name
                # print(table_head_list[l])
                headid = "header" + headname
                target = browser.find_element(By.ID, headid)
                browser.execute_script("arguments[0].scrollIntoView();", target)
                time.sleep(3)
                target2 = table_head_list[l].find_element(By.TAG_NAME, "mat-icon")
                browser.execute_script("arguments[0].click();", target2)
                time.sleep(3)
                select_dic = func_for_table(browser).test_filtersearch(table_head_list[l], 'ac')
                browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + head_name + "_search.png")
                time.sleep(2)
                for selectorder in select_dic['search_list']:
                    searchresult = re.findall(r'ac', selectorder, re.I)
                    assert len(searchresult) != 0
                for noselect in select_dic['no_search_list']:
                    noresult = re.findall(r'ac', noselect, re.I)
                    assert len(noresult) == 0
                target3 = browser.find_element(By.XPATH, "/html/body/div[2]/div[1]")
                browser.execute_script("arguments[0].click();", target3)
                mat_pass = func_for_table(browser).test_selectAll(table_head_list[l])
if __name__ == '__main__':
    pytest.main(["test_VS580455.py"])

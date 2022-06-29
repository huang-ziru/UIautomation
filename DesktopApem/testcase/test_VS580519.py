# coding = utf-8
import time
from framework.common import Common
import pytest
from selenium.webdriver.common.by import By

class TestSort():
    def test_sort(self, browser):
        table_head_list = Common(browser).get_tablehead()
        for l in range(len(table_head_list)):
            for x in range(3):
                # asc, desc and restore data
                revers_data = Common(browser).get_revers(table_head_list[l])
                table_data_sort = Common(browser).get_table(1)
                head_name = table_head_list[l].find_elements(By.TAG_NAME, 'div')[2].text
                # processing the string to date of Date and End Date
                if head_name in ('Date', 'End Date'):
                    for h in range(len(table_data_sort)):
                        str_p = table_data_sort[h][l]
                        # if str_p == '':
                        #     dateTime_p = datetime.datetime.strptime('01/01/1000, 01:01:01 am', '%m/%d/%Y, %I:%M:%S %p')
                        # else:
                        #     dateTime_p = datetime.datetime.strptime(str_p, '%m/%d/%y, %I:%M:%S %p')
                        dateTime_p = Common(browser).dateSort(str_p)
                        table_data_sort[h][l] = str(dateTime_p)
                if head_name in ('Quantity', 'Rep.'):
                    for k in range(len(table_data_sort)):
                        data = table_data_sort[k][l]
                        if data == '':
                            table_data_sort[k][l] = 0
                        else:
                            data = data.replace(',', '')
                            table_data_sort[k][l] = float(data)
                # Sort each data according to the corresponding column
                table_data_desc = sorted(table_data_sort, key=lambda x: x[l], reverse=True)
                table_data_asc = sorted(table_data_sort, key=lambda x: x[l], reverse=False)
                # assert the datas showed in table equal the datas which the script sorted
                if revers_data == 'ascending':
                    browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + head_name + "_asc.png")
                    time.sleep(3)
                    assert table_data_sort == table_data_asc

                elif revers_data == 'descending':
                    browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + head_name + "_desc.png")
                    time.sleep(3)
                    assert table_data_sort == table_data_desc
        time.sleep(5)

if __name__ == '__main__':
    pytest.main(["-s", "test_VS580519.py"])


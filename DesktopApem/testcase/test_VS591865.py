# coding = utf-8
import time
from framework.common import Common
from framework.columsfunc import Func
import pytest
from selenium.webdriver.common.by import By
def test_sorttrack(browser):
    time.sleep(3)
    columns_list = ['checkAuto.', 'checkAssigned WkSt.', 'checkExecuting WkSt.', 'checkExecuting User', 'checkRepetition Count', 'checkUser RUDO', 'checkWkSt. RUDO']
    track = browser.find_elements(by=By.CSS_SELECTOR, value="mat-icon[data-mat-icon-name='double_arrow']")
    Common(browser).eleclick(track[0])
    time.sleep(3)
    Func(browser).visiblecols(columns_list)
    head_list = browser.find_elements(By.XPATH, "//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/thead/tr/th")
    for l in range(1, len(head_list)-1):
        for x in range(3):  # asc, desc and restore data
            revers_data = Common(browser).get_revers(head_list[l])
            table_data_sort = Common(browser).get_table(0)
            head_name = head_list[l].find_elements(By.TAG_NAME, 'div')[2].get_attribute('textContent')
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
    pytest.main(["-s", "test_VS591865.py"])
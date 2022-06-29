# coding = utf-8
import time
from framework.basefunc import MainPage
from framework.columsfunc import Func
import pytest


def test_sorttrack(browser):
    time.sleep(3)
    columns_list = ['checkAuto.', 'checkAssigned WkSt.', 'checkUser Status', 'checkExecuting WkSt.', 'checkExecuting User', 'checkRepetition Count', 'checkUser RUDO', 'checkWkSt. RUDO']
    track = browser.find_elements_by_css_selector("mat-icon[data-mat-icon-name='double_arrow']")
    MainPage(browser).eleclick(track[0])
    time.sleep(3)
    Func(browser).visiblecols(columns_list)
    head_list = browser.find_elements_by_xpath("//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/thead/tr/th")
    for l in range(1, len(head_list)):
        for x in range(3):  # asc, desc and restore data
            revers_data = MainPage(browser).get_revers(head_list[l])
            table_data_sort = MainPage(browser).get_table(0)
            head_name = head_list[l].find_elements_by_tag_name('div')[2].get_attribute('textContent')
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
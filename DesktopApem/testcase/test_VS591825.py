# coding = utf-8
import time
from selenium.webdriver.support.color import Color
from framework.common import Common
import pytest
from selenium.webdriver.common.by import By
def test_checkdefaultview(browser):
    time.sleep(3)
    track = browser.find_elements(by=By.CSS_SELECTOR, value="mat-icon[data-mat-icon-name='double_arrow']")
    Common(browser).eleclick(track[0])
    time.sleep(3)
    group = browser.find_elements(by=By.CSS_SELECTOR, value="mat-button-toggle-group[name='trackingPanel']>mat-button-toggle")
    # high lighted means shows table mode
    backcolor1 = group[0].value_of_css_property('background-color')
    assert Color.from_string(backcolor1) == Color.from_string('#0078c9')
    backcolor2 = group[1].value_of_css_property('background-color')
    assert Color.from_string(backcolor2) == Color.from_string('#ffffff')
    # Odd columns shows white, even columns shows grey
    table_tr_list = browser.find_elements(By.XPATH, "//tbody/tr")
    for i in range(len(table_tr_list)):
        backcolor = table_tr_list[i].value_of_css_property('background-color')
        # if the line is even lines
        if (i + 1) % 2 != 0:
            assert Color.from_string(backcolor) == Color.from_string('#ffffff')
        else:
            assert Color.from_string(backcolor) == Color.from_string('#f3f3f3')
    # The phases are sorted ascendant by No. column by default
    table_list = Common(browser).get_table(0)
    table_data_asc = sorted(table_list, key=lambda x: int(x[0]), reverse=False)
    assert table_list == table_data_asc
    # Check the phase with parameters in it, the phase name is a hyperlink
    browser.find_element(By.XPATH, "//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/tbody/tr[1]/td[2]/div[1]/div").click()
    time.sleep(3)
    assert "parameters" in browser.current_url







if __name__ == '__main__':
    pytest.main(["-s", "test_VS591825.py"])
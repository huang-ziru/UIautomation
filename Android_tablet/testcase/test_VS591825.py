# coding = utf-8
import time
from selenium.webdriver.support.color import Color
from framework.basefunc import MainPage
import pytest

def test_checkdefaultview(browser):
    time.sleep(3)
    track = browser.find_elements_by_css_selector("mat-icon[data-mat-icon-name='double_arrow']")
    MainPage(browser).eleclick(track[0])
    time.sleep(3)
    group = browser.find_elements_by_css_selector("mat-button-toggle-group[name='trackingPanel']>mat-button-toggle")
    # high lighted means shows table mode
    backcolor1 = group[0].value_of_css_property('background-color')
    assert Color.from_string(backcolor1) == Color.from_string('#0078c9')
    backcolor2 = group[1].value_of_css_property('background-color')
    assert Color.from_string(backcolor2) == Color.from_string('#ffffff')
    # The phases are sorted ascendant by No. column by default
    table_list = MainPage(browser).get_table(0)
    table_data_asc = sorted(table_list, key=lambda x: int(x[0]), reverse=False)
    assert table_list == table_data_asc
    # The default columns shows: No., Phase, Status, Status icon
    default_head = browser.find_elements_by_xpath("//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/thead/tr/th")
    assert len(default_head) == 4
    # print(default_head)
    for i in range(len(default_head)):
        head_name = default_head[i].find_element_by_xpath("div/div/div").get_attribute('textContent')
        assert head_name in ("No.", "Phase", "Status", "")
    # Check the phase with parameters in it, the phase name is a hyperlink
    browser.find_element_by_xpath("//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/tbody/tr[1]/td[2]/div[1]/div").click()
    time.sleep(3)
    assert "parameters" in browser.current_url







if __name__ == '__main__':
    pytest.main(["-s", "test_VS591825.py"])
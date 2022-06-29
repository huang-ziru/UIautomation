# coding = utf-8
import time
from framework.basefunc import MainPage
import pytest

def test_gotoTrack(browser):
    time.sleep(3)
    track = browser.find_elements_by_css_selector("mat-icon[data-mat-icon-name='double_arrow']")
    MainPage(browser).eleclick(track[0])
    assert "tracking" in browser.current_url
    elementObj = browser.find_element_by_xpath("/html/body/app-root/div/app-navigation")
    browser.execute_script("arguments[0].className='show-nav'", elementObj)
    browser.find_element_by_css_selector("mat-icon[data-mat-icon-name='process_order']").click()
    time.sleep(2)
    elementObj = browser.find_element_by_xpath("/html/body/app-root/div/app-navigation")
    browser.execute_script("arguments[0].className='show-nav'", elementObj)
    browser.find_element_by_css_selector("mat-icon[data-mat-icon-name='tracking']").click()
    assert "tracking" in browser.current_url
if __name__ == '__main__':
    pytest.main(["-s", "test_VS591822.py"])
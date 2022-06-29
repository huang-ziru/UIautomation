# coding = utf-8
import configparser
import time
import pytest
from framework.basefunc import MainPage

class Testtitle_bar():
    def test_GatherOn(self, browser):
        elementObj = browser.find_element_by_xpath("/html/body/app-root/div/app-navigation")
        browser.execute_script("arguments[0].className='show-nav'", elementObj)
        time.sleep(2)
        browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='settings']").click()
        switch = browser.find_element_by_xpath("//div[@class='show-navigation'][5]/div/div[2]/mat-slide-toggle")
        if switch.find_element_by_tag_name('input').get_attribute('aria-checked') == 'false':
            MainPage(browser).eleclick(switch)
        time.sleep(5)
        elementObj = browser.find_element_by_xpath("/html/body/app-root/div/app-navigation")
        browser.execute_script("arguments[0].className='show-nav'", elementObj)
        time.sleep(2)
        assert MainPage(browser).is_element_showed("mat-icon[data-mat-icon-name='process_order']") is False
        assert MainPage(browser).is_element_showed("mat-icon[data-mat-icon-name='tracking']") is False
        assert MainPage(browser).is_element_showed("mat-icon[data-mat-icon-name='consolidated']") is True
        assert len(browser.find_elements_by_xpath("/html/body/app-root/div/app-navigation/nav/div[2]/div/div/a")) == 2
        browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='consolidated']").click()
        time.sleep(2)
        td = browser.find_elements_by_xpath("/html/body/app-root/div/div/app-consolidated-view/div/div[2]/table/tbody/tr/td[1]")
        order_td = MainPage(browser).td_data(td)
        order_list_name = MainPage(browser).table_ordername(order_td)
        for order_name in ['FROM_RPL', '2BPLS', 'START', 'X_ORDER']:
            assert order_name in order_list_name
        browser.find_element_by_css_selector("mat-icon[svgicon='fullscreen']").click()
        time.sleep(1)
        elementObj = browser.find_element_by_xpath("/html/body/app-root/div/app-navigation")
        browser.execute_script("arguments[0].className='show-nav'", elementObj)
        time.sleep(2)
        assert MainPage(browser).is_element_showed("mat-icon[data-mat-icon-name='consolidated']") is True
        assert len(browser.find_elements_by_xpath("/html/body/app-root/div/app-navigation/nav/div[2]/div/div/a")) == 2
        for order_name in ['FROM_RPL', '2BPLS', 'START', 'X_ORDER']:
            assert order_name in order_list_name

    def test_GatherOff(self, browser):
        elementObj = browser.find_element_by_xpath("/html/body/app-root/div/app-navigation")
        browser.execute_script("arguments[0].className='show-nav'", elementObj)
        time.sleep(2)
        browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='settings']").click()
        switch = browser.find_element_by_xpath("//div[@class='show-navigation'][5]/div/div[2]/mat-slide-toggle")
        if switch.find_element_by_tag_name('input').get_attribute('aria-checked') == 'true':
            MainPage(browser).eleclick(switch)
        time.sleep(5)
        assert MainPage(browser).is_element_showed("mat-icon[data-mat-icon-name='process_order']") is True
        assert MainPage(browser).is_element_showed("mat-icon[data-mat-icon-name='tracking']") is True

if __name__ == '__main__':
    pytest.main(["-s", "test_VS591827.py"])


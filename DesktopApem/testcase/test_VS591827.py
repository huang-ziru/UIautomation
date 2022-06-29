# coding = utf-8
from selenium.webdriver.common.by import By
import time
import pytest
from framework.common import Common
from framework.basefunc import MainPage
class Testtitle_bar():
    def test_GatherOn(self, browser):
        browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='settings']").click()
        switch = browser.find_element(By.XPATH, "//div[@class='show-navigation'][5]/div/div[2]/mat-slide-toggle")
        if switch.find_element(By.TAG_NAME, 'input').get_attribute('aria-checked') == 'false':
            Common(browser).eleclick(switch)
        time.sleep(5)
        assert MainPage(browser).is_element_showed("mat-icon[data-mat-icon-name='process_order']") is False
        assert MainPage(browser).is_element_showed("mat-icon[data-mat-icon-name='tracking']") is False
        assert MainPage(browser).is_element_showed("mat-icon[data-mat-icon-name='consolidated']") is True
        assert len(browser.find_elements(by=By.CSS_SELECTOR, value="body > app-root > div > app-sidenav > nav >a")) == 2
        browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='consolidated']").click()
        time.sleep(2)
        td = browser.find_elements(By.XPATH, "/html/body/app-root/div/app-consolidated-view/div/div[2]/table/tbody/tr/td[1]")
        order_td = Common(browser).td_data(td)
        order_list_name = Common(browser).table_ordername(order_td)
        for order_name in ['2BPLS', 'START', 'X_ORDER', 'FOR_BING']:
        #     assert order_name in order_list_name
            assert order_name in order_list_name
        browser.find_element(By.CSS_SELECTOR, value="mat-icon[svgicon='fullscreen']").click()
        time.sleep(1)
        assert MainPage(browser).is_element_showed("mat-icon[data-mat-icon-name='consolidated']") is True
        assert len(browser.find_elements(by=By.CSS_SELECTOR, value="body > app-root > div > app-sidenav > nav >a")) == 2
        for order_name in ['2BPLS', 'START', 'X_ORDER', 'FOR_BING']:
            assert order_name in order_list_name
        browser.get_screenshot_as_file(r"..\\report\\result_picture\\titlebar_con.png")
        # restore data
        browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='settings']").click()
        switch = browser.find_element(By.XPATH, "//div[@class='show-navigation'][5]/div/div[2]/mat-slide-toggle")
        if switch.find_element(By.TAG_NAME, 'input').get_attribute('aria-checked') == 'true':
            Common(browser).eleclick(switch)

    def test_GatherOff(self, browser):
        browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='settings']").click()
        switch = browser.find_element(By.XPATH, "//div[@class='show-navigation'][5]/div/div[2]/mat-slide-toggle")
        if switch.find_element(By.TAG_NAME, 'input').get_attribute('aria-checked') == 'true':
            Common(browser).eleclick(switch)
        time.sleep(5)
        browser.get_screenshot_as_file(r"..\\report\\result_picture\\titlebar.png")
        assert MainPage(browser).is_element_showed("mat-icon[data-mat-icon-name='process_order']") is True
        assert MainPage(browser).is_element_showed("mat-icon[data-mat-icon-name='tracking']") is True

if __name__ == '__main__':
    pytest.main(["-s", "test_VS591827.py"])


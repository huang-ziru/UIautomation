# coding = utf-8
import time
import pytest
from framework.basefunc import MainPage
from appium.webdriver.common.touch_action import TouchAction
class Testtitle_bar():
    # def test_AuditReason(self, browser):
    #     elementObj = browser.find_element_by_xpath("/html/body/app-root/div/app-navigation")
    #     browser.execute_script("arguments[0].className='show-nav'", elementObj)
    #     time.sleep(2)
    #     browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='settings']").click()
    #     mouse = browser.find_element_by_xpath("//mat-icon[@svgicon='info']")
    #     TouchAction(browser).long_press(mouse).wait(3000).perform()
    #     time.sleep(3)
    #     hover_text = browser.find_element_by_xpath("//mat-tooltip-component/div").text
    #     assert "Set a standard audit reason to be used when performing any audit or choose for the system to not ask you what your reason is at all." == hover_text

    def test_select(self, browser):
        elementObj = browser.find_element_by_xpath("/html/body/app-root/div/app-navigation")
        browser.execute_script("arguments[0].className='show-nav'", elementObj)
        time.sleep(2)
        setting = browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='settings']")
        MainPage(browser).eleclick(setting)
        browser.find_element_by_xpath("//div[@class='show-navigation']/mat-form-field/div/div[1]/div/input").send_keys("test")
        checkbox = browser.find_element_by_xpath("//input[@type='checkbox']")
        if checkbox.get_attribute('aria-checked') == 'false':
            MainPage(browser).eleclick(checkbox)
        time.sleep(5)
        browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='process_order']").click()
        time.sleep(2)
        browser.find_elements_by_css_selector("div[class ~= 'order-with-param']")[0].click()
        time.sleep(2)
        phase_ele = browser.find_element_by_xpath("//app-parameters/div[3]/div[1]/cdk-tree/cdk-nested-tree-node[1]/button/span[1]/mat-icon")
        MainPage(browser).eleclick(phase_ele)
        browser.find_element_by_css_selector("div.ng-star-inserted").find_element_by_tag_name("input").send_keys('2')
        time.sleep(2)
        ok = browser.find_element_by_xpath("//span[text()=' OK ']/..")
        MainPage(browser).eleclick(ok)
        time.sleep(2)
        assert "process-order" in browser.current_url
    #
    def test_no_select(self, browser):
        elementObj = browser.find_element_by_xpath("/html/body/app-root/div/app-navigation")
        browser.execute_script("arguments[0].className='show-nav'", elementObj)
        time.sleep(2)
        setting = browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='settings']")
        MainPage(browser).eleclick(setting)
        browser.find_element_by_xpath("//div[@class='show-navigation']/mat-form-field/div/div[1]/div/input").send_keys("test")
        checkbox = browser.find_element_by_xpath("//input[@type='checkbox']")
        if checkbox.get_attribute('aria-checked') == 'true':
            MainPage(browser).eleclick(checkbox)
        time.sleep(5)
        browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='process_order']").click()
        time.sleep(2)
        browser.find_elements_by_css_selector("div[class ~= 'order-with-param']")[0].click()
        time.sleep(2)
        phase_ele = browser.find_element_by_xpath("//app-parameters/div[3]/div[1]/cdk-tree/cdk-nested-tree-node[1]/button/span[1]/mat-icon")
        MainPage(browser).eleclick(phase_ele)
        browser.find_element_by_css_selector("div.ng-star-inserted").find_element_by_tag_name("input").send_keys('2')
        ok = browser.find_element_by_xpath("//span[text()=' OK ']/..")
        MainPage(browser).eleclick(ok)
        time.sleep(2)
        reason = browser.find_element_by_xpath("//*[@id='title']").get_attribute('textContent')
        assert "Audit Reason" in reason

if __name__ == '__main__':
    pytest.main(["-s", "test_VS591770.py"])


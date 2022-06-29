# coding = utf-8
import time
import pytest
from selenium.webdriver import ActionChains
from framework.common import Common
from selenium.webdriver.common.by import By
class Testtitle_bar():
    def test_AuditReason(self, browser):
        browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='settings']").click()
        mouse = browser.find_element(By.XPATH, "//mat-icon[@svgicon='info']")
        ActionChains(browser).move_to_element(mouse).perform()
        hover_text = browser.find_element(By.XPATH, "/html/body/div[2]").text
        assert "Set a standard audit reason to be used when performing any audit or choose for the system to not ask you what your reason is at all." == hover_text

    def test_select(self, browser):
        setting = browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='settings']")
        Common(browser).eleclick(setting)
        browser.find_element(By.XPATH, "/html/body/app-root/div/app-settings/div/div[2]/mat-form-field/div/div[1]/div/input").send_keys("test")
        checkbox = browser.find_element(By.XPATH, "//input[@type='checkbox']")
        if checkbox.get_attribute('aria-checked') == 'false':
            Common(browser).eleclick(checkbox)
        time.sleep(5)
        browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='process_order']").click()
        time.sleep(2)
        browser.find_elements(by=By.CSS_SELECTOR, value="div[class ~= 'order-with-param']")[0].click()
        time.sleep(2)
        phase_ele = browser.find_element(By.XPATH, "//app-parameters/div[3]/div[1]/cdk-tree/cdk-nested-tree-node[1]/button/span[1]/mat-icon")
        Common(browser).eleclick(phase_ele)
        browser.find_element(By.CSS_SELECTOR, value="div.ng-star-inserted").find_element(By.TAG_NAME, "input").send_keys('2')
        browser.find_element(By.XPATH, "//span[text()=' OK ']/..").click()
        time.sleep(2)
        assert "process-order" in browser.current_url
        # restore data
        setting = browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='settings']")
        Common(browser).eleclick(setting)
        browser.find_element(By.XPATH, "/html/body/app-root/div/app-settings/div/div[2]/mat-form-field/div/div[1]/div/input").send_keys("test")
        checkbox = browser.find_element(By.XPATH, "//input[@type='checkbox']")
        if checkbox.get_attribute('aria-checked') == 'true':
            Common(browser).eleclick(checkbox)

    def test_no_select(self, browser):
        setting = browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='settings']")
        Common(browser).eleclick(setting)
        browser.find_element(By.XPATH, "/html/body/app-root/div/app-settings/div/div[2]/mat-form-field/div/div[1]/div/input").send_keys("test")
        checkbox = browser.find_element(By.XPATH, "//input[@type='checkbox']")
        if checkbox.get_attribute('aria-checked') == 'true':
            Common(browser).eleclick(checkbox)
        time.sleep(5)
        browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='process_order']").click()
        time.sleep(2)
        browser.find_elements(by=By.CSS_SELECTOR, value="div[class ~= 'order-with-param']")[0].click()
        time.sleep(2)
        phase_ele = browser.find_element(By.XPATH, "//app-parameters/div[3]/div[1]/cdk-tree/cdk-nested-tree-node[1]/button/span[1]/mat-icon")
        Common(browser).eleclick(phase_ele)
        browser.find_element(By.CSS_SELECTOR, value="div.ng-star-inserted").find_element(By.TAG_NAME, "input").send_keys('2')
        browser.find_element(By.XPATH, "//span[text()=' OK ']/..").click()
        time.sleep(2)
        reason = browser.find_element(By.XPATH, "//*[@id='title']").get_attribute('textContent')
        assert "Audit Reason" in reason

if __name__ == '__main__':
    pytest.main(["-s", "test_VS591770.py"])


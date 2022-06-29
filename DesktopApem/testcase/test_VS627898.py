# coding = utf-8
import time
from framework.common import Common
import pytest
from selenium.webdriver.common.by import By
def test_Check_structure(browser):
    time.sleep(10)
    order_ele = browser.find_element(By.XPATH, "//div[contains(text(),'2BPLS')]")
    # Click this order name
    order_ele.click()
    time.sleep(3)
    # User can input the field to change the value
    phase_ele = browser.find_element(By.XPATH, "//button[@aria-label='Toggle PHASE57']")
    Common(browser).eleclick(phase_ele)
    # Click ">" icons to  expand the following elements.
    assert browser.find_element(By.XPATH, "//button[@aria-label='Toggle PHASE57']/..").get_attribute("aria-expanded") == 'true'
    assert browser.find_element(By.XPATH, "//button[@aria-label='Toggle PHASE57']/../div[2]").get_attribute("class") == ''
    before_value = browser.find_element(By.XPATH, "//span[contains(text(),'TEMP')]/../mat-form-field/div/div/div/input").get_attribute("value")
    browser.find_element(By.XPATH, "//span[contains(text(),'TEMP')]/../mat-form-field/div/div/div/input").clear()
    browser.find_element(By.XPATH, "//span[contains(text(),'TEMP')]/../mat-form-field/div/div/div/input").send_keys('66')
    time.sleep(2)
    browser.find_element(By.XPATH, "/html/body/app-root/div").click()
    after_value = browser.find_element(By.XPATH, "//span[contains(text(),'TEMP')]/../mat-form-field/div/div/div/input").get_attribute("value")
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\change_value.png")
    assert before_value != after_value
    assert after_value == '66'
    # click "V" icon to collapse the following elements.
    phase_ele = browser.find_element(By.XPATH, "//button[@aria-label='Toggle PHASE57']")
    Common(browser).eleclick(phase_ele)
    assert browser.find_element(By.XPATH, "//button[@aria-label='Toggle PHASE57']/..").get_attribute("aria-expanded") == 'false'
    assert browser.find_element(By.XPATH, "//button[@aria-label='Toggle PHASE57']/../div[2]").get_attribute("class") == 'example-tree-invisible'
    # Click "+" icon to add elements
    browser.find_element(By.XPATH, "//button[@aria-label='Toggle PHASE51']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[@aria-label='Toggle PHASE51']/../div[2]/cdk-nested-tree-node[1]/button").click()
    time.sleep(3)
    Yes_color = browser.find_element(By.XPATH, "//input[@aria-checked='true']/..").value_of_css_property('background-color')
    No_color = browser.find_element(By.XPATH, "//input[@aria-checked='false']/..").value_of_css_property('background-color')
    # Check the grey stands for No, the blue stands for Yes
    assert Yes_color == 'rgba(38, 152, 251, 0.54)'
    assert No_color == 'rgba(0, 0, 0, 0)'
    Valuelist = browser.find_elements(By.XPATH, "//div[@class='mat-slide-toggle-thumb']/../../../../../../span")
    browser.find_element(By.XPATH, "//span/mat-icon[text()='add']").click()
    time.sleep(3)
    # click cancel add
    # browser.find_element(By.XPATH, "//*[@id='error-message-dialog']/div/div[3]/button[1]").click()
    # time.sleep(2)
    # browser.get_screenshot_as_file(r"..\\report\\result_picture\\addelement.png")
    # cancel_add = browser.find_elements(By.XPATH, "//div[@class='mat-slide-toggle-thumb']/../../../../../../span")
    # click add OK
    # browser.find_element(By.XPATH, "//span/mat-icon[text()='add']").click()
    # time.sleep(3)
    # browser.find_element(By.XPATH, "//*[@id='error-message-dialog']/div/div[3]/button[2]").click()
    # time.sleep(5)
    Valuelist_add = browser.find_elements(By.XPATH, "//div[@class='mat-slide-toggle-thumb']/../../../../../../span")
    # assert len(Valuelist) == len(cancel_add)
    assert len(Valuelist_add) == len(Valuelist)+1
    # Click "-" icon to delete elements
    Valuelist_add[2].click()
    browser.find_element(By.XPATH, "//span/mat-icon[text()='remove']").click()
    time.sleep(3)
    # click cancel remove
    # browser.find_element(By.XPATH, "//*[@id='error-message-dialog']/div/div[3]/button[1]").click()
    # time.sleep(2)
    # cancel_remove = browser.find_elements(By.XPATH, "//div[@class='mat-slide-toggle-thumb']/../../../../../../span")
    # click remove ok
    # Valuelist_add[2].click()
    # browser.find_element(By.XPATH, "//span/mat-icon[text()='remove']").click()
    # time.sleep(3)
    # browser.find_element(By.XPATH, "//*[@id='error-message-dialog']/div/div[3]/button[2]").click()
    # time.sleep(5)
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\deleteelement.png")
    Valuelist_remove = browser.find_elements(By.XPATH, "//div[@class='mat-slide-toggle-thumb']/../../../../../../span")
    # assert len(Valuelist_add) == len(cancel_remove)
    assert len(Valuelist_remove) == len(Valuelist_add) - 1
    # for array type
    phasename_list = browser.find_elements(By.XPATH, "//cdk-tree/cdk-nested-tree-node/div[1]/div")
    phasenames = []
    for phasename in phasename_list:
        phasenames.append(phasename.get_attribute('textContent'))
    # click to "Tracking" page - Phase list
    browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='tracking']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//*[@id='error-message-dialog']/div/div[3]/button[2]").click()
    time.sleep(3)
    # get the phase name of the order
    phase_list = browser.find_elements(By.XPATH, "//div[@class = 'phase-name-text']")
    phase_names = []
    for phase in phase_list:
        phase_names.append(phase.get_attribute('textContent'))
    # the phase name should show on the first parent level
    for name in phasenames:
        assert name in phase_names




if __name__ == '__main__':
    pytest.main(["-s", "test_VS627898.py"])
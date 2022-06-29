# # coding = utf-8
# import time
# from selenium.webdriver.common.keys import Keys
# from framework.common import Common
# from framework.basefunc import MainPage
# from selenium.webdriver.common.by import By
# import pytest
# def test_Footer(browser):
#     time.sleep(4)
#     order_ele = browser.find_element(By.XPATH, "//div[contains(text(),'FOR_GML')]/../..")
#     order_ele.find_elements(By.TAG_NAME, "td")[-1].click()
#     time.sleep(5)
#     phase_ele1 = browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='phase_state_enabled']")
#     phase_name1 = phase_ele1.find_element(By.XPATH, "./../../../../../../td[2]/div[1]/div").text
#     Common(browser).eleclick(phase_ele1)
#     time.sleep(5)
#     # On execution page, execute a basic phase of an order, click blue 'OK' button
#     browser.find_element(By.XPATH, "//*[@id='screen']/app-aebrs-footer/button").click()
#     time.sleep(3)
#     assert MainPage(browser).is_element_showed("mat-dialog-container") is True
#     # click cancel
#     cancel = browser.find_element(By.XPATH, "//button[@id='INSTRUCTION.cmpFooter.btnCancel']")
#     Common(browser).eleclick(cancel)
#     time.sleep(2)
#     browser.find_element(By.XPATH, "//div[@id='dialog']/div/div[3]/button[1]").click()
#     time.sleep(5)
#     assert 'tracking' in browser.current_url
#     phase_ele2 = browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='phase_state_enabled']")
#     phase_name2 = phase_ele2.find_element(By.XPATH, "./../../../../../../td[2]/div[1]/div").text
#     assert phase_name1 == phase_name2
#     # click enter
#     Common(browser).eleclick(phase_ele2)
#     time.sleep(5)
#     browser.find_element(By.XPATH, "//*[@id='screen']/app-aebrs-footer/button").click()
#     time.sleep(5)
#     # enter userId and password
#     browser.find_element(By.XPATH, "//input[@id='INSTRUCTION.cmpFooter.txtUserId']").click()
#     browser.find_element(By.XPATH, "//input[@id='INSTRUCTION.cmpFooter.txtUserId']").send_keys("corp\\qaone")
#     browser.find_element(By.XPATH, "//input[@id='INSTRUCTION.cmpFooter.pwdSignature']").click()
#     browser.find_element(By.XPATH, "//input[@id='INSTRUCTION.cmpFooter.pwdSignature']").send_keys("Aspen111")
#     browser.find_element(By.XPATH, "//input[@id='INSTRUCTION.cmpFooter.pwdSignature']").send_keys(Keys.ENTER)
#     time.sleep(10)
#     assert 'tracking' in browser.current_url
#     statuslist = browser.find_elements(By.XPATH, "//mat-icon")
#     for status in statuslist:
#         assert 'finished' in status.get_attribute('data-mat-icon-name') or 'planned' in status.get_attribute('data-mat-icon-name')
#
# if __name__ == '__main__':
#     pytest.main(["-s", "test_VS629827.py"])
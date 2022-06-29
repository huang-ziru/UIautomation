# coding = utf-8
import time
from framework.common import Common
from framework.basefunc import MainPage
import pytest
from selenium.webdriver.common.by import By
def test_Phase_excute(browser):
    time.sleep(5)
    order_ele = browser.find_element(By.XPATH, "//div[contains(text(),'START')]/../..")
    order_ele.find_elements(By.TAG_NAME, "td")[-1].click()
    time.sleep(6)
    # phase_list = browser.find_elements(By.XPATH, "//div/a")
    # phase_name = phase_list[1].find_element(By.XPATH, "./../../../../../td[2]/div/div").get_attribute('textContent')
    phase_list = browser.find_element(By.XPATH, "//div/a")
    phase_name = phase_list.find_element(By.XPATH, "./../../../../../td[2]/div/div").get_attribute('textContent')
    Common(browser).eleclick(phase_list.find_element(By.TAG_NAME, "mat-icon"))
    time.sleep(75)
    # cancel = browser.find_element(By.XPATH, "//*[@id='screen']/app-aebrs-button[2]/button")
    cancel = browser.find_element(By.XPATH, "// *[ @ id = 'Main.CancelButton0']")
    # click "Cancel" button
    Common(browser).eleclick(cancel)
    # A confirmation message pop up.
    time.sleep(2)
    assert MainPage(browser).is_element_showed("div#dialog") is True
    # Click  'NO'  then it stay in the current execution page.
    browser.find_element(By.XPATH, "//*[@id='dialog']/div/div[3]/button[2]").click()
    time.sleep(1)
    assert 'execution' in browser.current_url
    # Click 'Yes' then the page goes to phase list or PFC which you click in.
    Common(browser).eleclick(cancel)
    time.sleep(10)
    browser.find_element(By.XPATH, "//*[@id='dialog']/div/div[3]/button[1]").click()
    time.sleep(30)
    browser.refresh()
    assert 'tracking' in browser.current_url
    # Click "OK" button
    # phase_list1 = browser.find_elements(By.XPATH, "//div/a")
    # Common(browser).eleclick(phase_list1[1].find_element(By.TAG_NAME, "mat-icon"))
    phase_list = browser.find_element(By.XPATH, "//div/a")
    phase_name = phase_list.find_element(By.XPATH, "./../../../../../td[2]/div/div").get_attribute('textContent')
    time.sleep(30)
    Common(browser).eleclick(phase_list.find_element(By.TAG_NAME, "mat-icon"))
    time.sleep(70)
    ok = browser.find_element(By.XPATH, "//*[@id='Main.OkButton0']")
    Common(browser).eleclick(ok)
    time.sleep(30)
    browser.refresh()
    # The page goes to phase list or PFC which you click in, and the phase state is "Finished".
    assert 'tracking' in browser.current_url
    phase_name_list = browser.find_elements(By.XPATH, "//div[@class='phase-name-text']")
    for phasename in phase_name_list:
        if phasename == phase_name:
            phase_path = "//div[@class='phase-name-text' and text()=\'" + phase_name + "\']/../../../td[3]"
            phase_ele = browser.find_element(By.XPATH, phase_path)
            phase_state = phase_ele.get_attribute('textContent')
            assert 'Finished' == phase_state
            browser.get_screenshot_as_file(r"..\\report\\result_picture\\executeOk_629854.png")
if __name__ == '__main__':
    pytest.main(["-s", "test_VS629854.py"])
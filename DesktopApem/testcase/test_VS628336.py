# coding = utf-8
import time
from framework.common import Common
import pytest
from selenium.webdriver.common.by import By
def test_Breadcrumb(browser):
    time.sleep(4)
    # check shows the order name, batchcode
    order_ele = browser.find_element(By.XPATH, "//div[contains(text(),'START')]/../..")
    order_name = browser.find_element(By.XPATH, "//div[contains(text(),'START')]").text
    order_ele.find_elements(By.TAG_NAME, "td")[-1].click()
    time.sleep(5)
    colums_list = Common(browser).get_tablehead()
    print(colums_list)
    phase_list = browser.find_elements(By.XPATH, "//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/tbody/tr/td[12]/div/div/div/a/mat-icon")
    select_phase = phase_list[0].find_element(By.XPATH, "./../../../../../../td[2]/div[1]/div").text
    Common(browser).eleclick(phase_list[0])
    time.sleep(5)
    # exe = browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='phase_state_executing']")
    # select_phase = browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='phase_state_executing']/parent::*/parent::*/parent::*/parent::*/parent::*/td[2]/div[1]/div").text
    # Common(browser).eleclick(exe)
    # time.sleep(5)
    ordername = browser.find_element(By.XPATH, "//*[@id='order']").text
    assert order_name == ordername[7::]
    #  check shows the phase name.
    phasename = browser.find_element(By.XPATH, "/html/body/app-root/div/app-execution/div/div[1]/div").text
    assert select_phase == phasename
    #  go back to tracking list page.
    browser.find_element(By.ID, 'order').click()
    assert "tracking" in browser.current_url
    # the phase state is executing on phase list
    time.sleep(5)
    phase_list = browser.find_elements(By.XPATH, "//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/tbody/tr/td[2]/div[1]/div")
    count = 1
    for phase in phase_list:
        if phase.get_attribute('textContent') == phasename:
            state_xpath = "//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/tbody/tr[" + str(count) + "]"
            phase_ele = browser.find_element(By.XPATH, state_xpath).find_element(By.CSS_SELECTOR, value="td[class ~= 'cdk-column-STATUS']")
            phase_state = phase_ele.get_attribute('textContent')
            assert phase_state == 'Executing'
        else:
            count = count + 1


if __name__ == '__main__':
    pytest.main(["-s", "test_VS628336.py"])
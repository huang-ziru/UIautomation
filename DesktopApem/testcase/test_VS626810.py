# coding = utf-8
import time
from framework.common import Common
import pytest
from selenium.webdriver.common.by import By
def test_IconStatus(browser):
    time.sleep(2)
    order_ele = browser.find_element(By.XPATH, "//div[contains(text(),'FROM_RPL')]/../..")
    order_ele.find_elements(By.TAG_NAME, "td")[-1].click()
    time.sleep(2)
    Status = browser.find_elements(by=By.CSS_SELECTOR, value="td[class ~= 'cdk-column-STATUS']")
    Exe_icon = browser.find_elements(by=By.CSS_SELECTOR, value="td[class ~= 'cdk-column-EXECUTION']")
    for i in range(len(Status)):
        phase_status = Status[i].get_attribute('textContent')
        icon_name = Exe_icon[i].find_element(By.TAG_NAME, "mat-icon").get_attribute('data-mat-icon-name')
        if phase_status == 'Ready':
            assert 'enabled' in icon_name
        elif phase_status == 'Not ready':
            assert 'planned' in icon_name
        else:
            assert phase_status.lower() in icon_name

    # consolidated mode
    browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='settings']").click()
    switch = browser.find_element(By.XPATH, "//div[@class='show-navigation'][5]/div/div[2]/mat-slide-toggle")
    if switch.find_element(By.TAG_NAME, 'input').get_attribute('aria-checked') == 'false':
        Common(browser).eleclick(switch)
    time.sleep(5)
    browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='consolidated']").click()
    Con_Status = browser.find_elements(by=By.CSS_SELECTOR, value="td[class ~= 'cdk-column-STATUS']")
    Con_Exe_icon = browser.find_elements(by=By.CSS_SELECTOR, value="td[class ~= 'cdk-column-EXECUTION']")
    for j in range(len(Con_Status)):
        phase_status = Status[j].get_attribute('textContent')
        icon_name = Con_Exe_icon[j].find_element(By.TAG_NAME, "mat-icon").get_attribute('data-mat-icon-name')
        if phase_status == 'Ready':
            assert 'enabled' in icon_name
        elif phase_status == 'Not Ready':
            assert 'planned' in icon_name
        elif phase_status == 'Executing locally':
            assert 'executing' in icon_name
        else:
            assert phase_status.lower() in icon_name
    # restore data
    browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='settings']").click()
    switch = browser.find_element(By.XPATH, "//div[@class='show-navigation'][5]/div/div[2]/mat-slide-toggle")
    Common(browser).eleclick(switch)




if __name__ == '__main__':
    pytest.main(["-s", "test_VS626810.py"])
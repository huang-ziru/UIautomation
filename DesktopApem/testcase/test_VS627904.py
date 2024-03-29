# coding = utf-8
from framework.constant import get_caseID
import time, re
from framework.common import Common
import pytest
from selenium.webdriver.common.by import By
def test_CheckDetails(browser):
    time.sleep(10)
    order_ele = browser.find_element(By.XPATH, "//div[contains(text(),'2BPLS')]")
    # Click this order name
    order_ele.click()
    time.sleep(3)
    # User can input the field to change the value
    phase_ele = browser.find_element(By.XPATH, "//button[@aria-label='Toggle PHASE57']")
    Common(browser).eleclick(phase_ele)
    paramEle = browser.find_element(By.XPATH, "//div[@class='ng-star-inserted']/div/span").text
    paramtitle = re.split(':', paramEle)[0]
    browser.find_elements(By.XPATH, "//div[@class='ng-star-inserted']/div/span")[0].click()
    time.sleep(2)
    phase_title = browser.find_element(By.XPATH, "//mat-card-title/div").text
    phaser_descrip = browser.find_element(By.XPATH, "//mat-card-subtitle[@class='mat-card-subtitle']/p").text
    assert phase_title == paramtitle
    assert phaser_descrip == 'Temperature'
    properties = browser.find_elements(By.XPATH, "//mat-card-content")
    pro_list = ['No', 'Type', 'Range', 'Unit', 'Allow null', 'RUDO Planned', 'Rudo Active']
    proper_list = []
    for pro in properties:
        pro_name = re.split(':', pro.find_element(By.TAG_NAME, "div").get_attribute('textContent'))[0]
        proper_list.append(pro_name)
    # shows the properties of this parameter
    for proper in pro_list:
        assert proper in proper_list
    # click another parameter,the detail card updates
    browser.find_elements(By.XPATH, "//div[@class='ng-star-inserted']/div/span")[1].click()
    time.sleep(2)
    phase_title2 = browser.find_element(By.XPATH, "//mat-card-title/div").text
    phaser_descrip2 = browser.find_element(By.XPATH, "//mat-card-subtitle[@class='mat-card-subtitle']/p").text
    assert phase_title2 == 'VOL'
    assert phaser_descrip2 == 'Volume'

if __name__ == '__main__':
    pytest.main(["-s", "test_VS627904.py"])
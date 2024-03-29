# coding = utf-8
from framework.constant import get_caseID
import time
from framework.common import Common
from framework.basefunc import MainPage
import pytest
from selenium.webdriver.common.by import By
def test_goto_param(browser):
    time.sleep(2)
    order_ele = browser.find_element(By.XPATH, "//div[contains(text(),'2BPLS')]")
    # Check the underline shows for this order to indicate this order has parameter in it.
    assert 'order-with-param' in order_ele.get_attribute('class')
    # Click this order name
    order_ele.click()
    time.sleep(3)
    # It goes to parameter page directly, and BPL1/Parameter, BPL2/Parameter tree structure shows on the left page
    phase_trees1 = browser.find_elements(By.XPATH, "//div[@class='tree-structure scroll-bar']/cdk-tree/cdk-nested-tree-node")
    assert len(phase_trees1) == 8
    # click to "Tracking" page - Phase list
    browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='tracking']").click()
    time.sleep(3)
    # Check if the underline shows for this phase (BPL1) to indicate this phase has parameter in it.
    phase_trees2 = browser.find_elements(By.XPATH, "//div[@class = 'collapse-text phase-name phase-with-param']/div")
    assert len(phase_trees2) == 8
    # click one phase name ,check do to the parameters page
    phase_name = phase_trees2[0].text
    Common(browser).eleclick(phase_trees2[0])
    time.sleep(4)
    assert 'parameters' in browser.current_url
    assert phase_name in browser.find_element(By.XPATH, "/html/body/app-root/div/app-parameters/div[2]").text
    assert MainPage(browser).is_element_showed("div[class~='tree-structure']") is True
    assert MainPage(browser).is_element_showed("div[class~='detail-card']") is True
    # tree_structure = browser.find_element(By.XPATH, "/html/body/app-root/div/app-parameters/div[3]/div[1]")
    # detail_card = browser.find_element(By.XPATH, "/html/body/app-root/div/app-parameters/div[3]/div[2]")
    # tree_rect = tree_structure.rect
    # detail_rect = detail_card.rect
    # print(tree_rect)
    # print(detail_rect)




if __name__ == '__main__':
    pytest.main(["-s", "test_VS627824.py"])
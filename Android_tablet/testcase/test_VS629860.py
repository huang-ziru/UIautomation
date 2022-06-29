# coding = utf-8
import time

from selenium.webdriver import ActionChains

from framework.basefunc import MainPage
import pytest
from framework.constant import login
def test_change_excute():
    browser = login()
    time.sleep(4)
    order_ele = browser.find_element_by_xpath("//div[contains(text(),'X_ORDER')]/../..")
    order_ele.find_elements_by_tag_name("td")[-1].click()
    time.sleep(2)
    phase_list = browser.find_elements_by_xpath("//div/a")
    phase_name = phase_list[1].find_element_by_xpath("./../../../../../td[2]/div/div").get_attribute('textContent')
    MainPage(browser).eleclick(phase_list[1].find_element_by_tag_name("mat-icon"))
    time.sleep(5)
    change_ele = browser.find_element_by_xpath("//*[@id='MAIN.Table002']")
    before_value = change_ele.get_attribute('value')
    MainPage(browser).eleclick(change_ele)
    time.sleep(1)
    MainPage(browser).eleclick(browser.find_element_by_xpath("//*[@id='MAIN.Table002']"))
    time.sleep(2)
    browser.find_element_by_xpath("//div[@class='cdk-overlay-pane']/div/mat-option[1]").click()
    time.sleep(1)
    after_value = browser.find_element_by_xpath("//*[@id='MAIN.Table002']").get_attribute('value')
    browser.close()
    new_driver = login()
    time.sleep(2)
    order_ele = new_driver.find_element_by_xpath("//div[contains(text(),'X_ORDER')]/../..")
    order_ele.find_elements_by_tag_name("td")[-1].click()
    time.sleep(2)
    phase_list = new_driver.find_elements_by_xpath("//div/a")
    phase_path = "//div[@class='phase-name-text' and text()=\'" + phase_name + "\']/../../../td[3]"
    phase_ele = new_driver.find_element_by_xpath(phase_path)
    phase_state = phase_ele.get_attribute('textContent')
    MainPage(new_driver).eleclick(phase_list[1].find_element_by_tag_name("mat-icon"))
    time.sleep(5)
    current_value = new_driver.find_element_by_xpath("//*[@id='MAIN.Table002']").get_attribute('value')
    # Check the changes are shown up.
    assert current_value != before_value
    assert current_value == after_value
    # the phase state is "Executing".
    assert 'Executing' == phase_state
    browser.quit()
if __name__ == '__main__':
    pytest.main(["-s", "test_VS629860.py"])
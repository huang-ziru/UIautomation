# coding = utf-8
import time
from framework.basefunc import MainPage
import pytest
def test_Phase_excute(browser):
    time.sleep(5)
    order_ele = browser.find_element_by_xpath("//div[contains(text(),'START')]/../..")
    order_ele.find_elements_by_tag_name("td")[-1].click()
    time.sleep(2)
    phase_list = browser.find_elements_by_xpath("//div/a")
    phase_name = phase_list[1].find_element_by_xpath("./../../../../../td[2]/div/div").get_attribute('textContent')
    MainPage(browser).eleclick(phase_list[1].find_element_by_tag_name("mat-icon"))
    time.sleep(5)
    cancel = browser.find_element_by_xpath("//*[@id='screen']/app-aebrs-button[2]/button")
    # click "Cancel" button
    MainPage(browser).eleclick(cancel)
    # A confirmation message pop up.
    time.sleep(2)
    assert MainPage(browser).is_element_showed("div#dialog") is True
    # Click  'NO'  then it stay in the current execution page.
    browser.find_element_by_xpath("//*[@id='dialog']/div/div[2]/button[2]").click()
    time.sleep(1)
    assert 'execution' in browser.current_url
    # Click 'Yes' then the page goes to phase list or PFC which you click in.
    MainPage(browser).eleclick(cancel)
    time.sleep(2)
    browser.find_element_by_xpath("//*[@id='dialog']/div/div[2]/button[1]").click()
    time.sleep(5)
    assert 'tracking' in browser.current_url
    # Click "OK" button
    phase_list1 = browser.find_elements_by_xpath("//div/a")
    MainPage(browser).eleclick(phase_list1[1].find_element_by_tag_name("mat-icon"))
    time.sleep(5)
    ok = browser.find_element_by_xpath("//*[@id='screen']/app-aebrs-button[1]/button")
    MainPage(browser).eleclick(ok)
    time.sleep(5)
    # The page goes to phase list or PFC which you click in, and the phase state is "Finished".
    assert 'tracking' in browser.current_url
    phase_name_list = browser.find_elements_by_xpath("//div[@class='phase-name-text']")
    for phasename in phase_name_list:
        if phasename == phase_name:
            phase_path = "//div[@class='phase-name-text' and text()=\'" + phase_name + "\']/../../../td[3]"
            phase_ele = browser.find_element_by_xpath(phase_path)
            phase_state = phase_ele.get_attribute('textContent')
            assert 'Finished' == phase_state
if __name__ == '__main__':
    pytest.main(["-s", "test_VS629854.py"])
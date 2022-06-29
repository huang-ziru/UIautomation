# coding = utf-8
import time
from framework.basefunc import MainPage
import pytest
def test_Breadcrumb(browser):
    time.sleep(4)
    # check shows the order name, batchcode
    order_ele = browser.find_element_by_xpath("//div[contains(text(),'START')]/../..")
    order_name = browser.find_element_by_xpath("//div[contains(text(),'START')]").text
    order_ele.find_elements_by_tag_name("td")[-1].click()
    time.sleep(5)
    phase_list = browser.find_elements_by_xpath("//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/tbody/tr/td[4]/div/div/div/a/mat-icon")
    select_phase = phase_list[0].find_element_by_xpath("./../../../../../../td[2]/div[1]/div").text
    MainPage(browser).eleclick(phase_list[0])
    time.sleep(5)
    # exe = browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='phase_state_executing']")
    # select_phase = browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='phase_state_executing']/parent::*/parent::*/parent::*/parent::*/parent::*/td[2]/div[1]/div").text
    # MainPage(browser).eleclick(exe)
    # time.sleep(5)
    ordername = browser.find_element_by_xpath("//*[@id='order']").text
    assert order_name == ordername[7::]
    #  check shows the phase name.
    phasename = browser.find_element_by_xpath("/html/body/app-root/div/div/app-execution/div/div[1]/div").text
    assert select_phase == phasename
    #  go back to tracking list page.
    browser.find_element_by_id('order').click()
    assert "tracking" in browser.current_url
    # the phase state is executing on phase list
    time.sleep(5)
    phase_list = browser.find_elements_by_xpath("//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/tbody/tr/td[2]/div[1]/div")
    count = 1
    for phase in phase_list:
        if phase.get_attribute('textContent') == phasename:
            state_xpath = "//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/tbody/tr[" + str(count) + "]/td[3]"
            phase_state = browser.find_element_by_xpath(state_xpath).text
            assert phase_state == 'Executing'
        else:
            count = count + 1


if __name__ == '__main__':
    pytest.main(["-s", "test_VS628336.py"])
# coding = utf-8
import time, re
from framework.common import Common
from framework.basefunc import MainPage
from framework.Login import login
import pytest
from selenium.webdriver.common.by import By
def test_Queue(browser):
    time.sleep(4)
    order_ele = browser.find_element(By.XPATH, "//div[contains(text(),'2BPLS')]/../..")
    order_ele.find_elements(By.TAG_NAME, "td")[-1].click()
    time.sleep(5)
    phase_list = browser.find_elements(By.XPATH, "//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/tbody/tr/td[11]/div/div/div/a/mat-icon")
    Common(browser).eleclick(phase_list[0])
    time.sleep(5)
    # Check the queue on execution page is 0 on the right of top page
    Queue_number1 = re.sub(r'\D', "", browser.find_element(By.XPATH, "//*[@id='queue-title']/div").text)
    assert Queue_number1 == '0'
    browser.find_element(By.XPATH, "//*[@id='order']").click()
    time.sleep(2)
    # Check the queue on PFC page, the queue is 1
    browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='graphic_view_blue']/../..").click()
    time.sleep(2)
    Queue_number2 = re.sub(r'\D', "", browser.find_element(By.XPATH, "//*[@id='queue-title']/div").text)
    assert Queue_number2 == '1'
    browser.close()
    # user2
    browser = login()
    MainPage(browser).logout()
    time.sleep(3)
    browser.find_element(By.XPATH, "/html/body/app-root/div/app-logout/div/button").click()
    time.sleep(3)
    browser.find_element(By.XPATH, '//*[@id="username"]').send_keys('corp\\qapart')
    browser.find_element(By.XPATH, '//input[@type="password"]').send_keys('QQQaaa000')
    browser.find_element(By.ID, 'signInBtn').click()
    time.sleep(4)
    order_ele = browser.find_element(By.XPATH, "//div[contains(text(),'2BPLS')]/../..")
    order_ele.find_elements(By.TAG_NAME, "td")[-1].click()
    time.sleep(5)
    # first executing
    phase_list2 = browser.find_elements(By.XPATH, "//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/tbody/tr/td[4]/div/div/div/a/mat-icon")
    phase_name2 = phase_list2[0].find_element(By.XPATH, "./../../../../../../td[2]/div[1]/div").text
    Common(browser).eleclick(phase_list2[0])
    time.sleep(5)
    # User2 also can see queue 0 on execution page
    Queue_number3 = re.sub(r'\D', "", browser.find_element(By.XPATH, "//*[@id='queue-title']/div").text)
    assert Queue_number3 == '0'
    browser.find_element(By.XPATH, "//*[@id='order']").click()
    time.sleep(2)
    # second executing
    phase_list3 = browser.find_elements(By.XPATH, "//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/tbody/tr/td[4]/div/div/div/a/mat-icon")
    phase_name3 = phase_list3[0].find_element(By.XPATH, "./../../../../../../td[2]/div[1]/div").text
    Common(browser).eleclick(phase_list3[0])
    time.sleep(5)
    # on execution page, the queue is 1.
    # on PFC graphic, the queue is 2,
    Queue_number4 = re.sub(r'\D', "", browser.find_element(By.XPATH, "//*[@id='queue-title']/div").text)
    assert Queue_number4 == '1'
    browser.find_element(By.XPATH, "//div[@class='queue']/mat-accordion/mat-expansion-panel/mat-expansion-panel-header").click()
    time.sleep(2)
    queue_phase = browser.find_element(By.XPATH, "//div[@class='phase-name']")
    phase_queue = re.split(':', queue_phase.text)[1]
    assert phase_name2 == phase_queue.strip()
    queue_phase.click()
    # It will go to the corresponding phase executing page.
    assert 'execution' in browser.current_url
    assert browser.find_element(By.XPATH, "/html/body/app-root/div/app-execution/div/div[1]/div").text == phase_name2
    browser.find_element(By.XPATH, "//*[@id='order']").click()
    time.sleep(2)
    PFC_Ele = browser.find_element(By.XPATH, "//mat-icon[@data-mat-icon-name='graphic_view_blue']/../..")
    Common(browser).eleclick(PFC_Ele)
    time.sleep(2)
    Queue_number4 = re.sub(r'\D', "", browser.find_element(By.XPATH, "//*[@id='queue-title']/div").text)
    assert Queue_number4 == '2'
    browser.quit()

if __name__ == '__main__':
    pytest.main(["-s", "test_VS628365.py"])
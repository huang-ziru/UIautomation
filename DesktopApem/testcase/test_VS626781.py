# coding = utf-8
import time, pytest
from selenium.webdriver.common.by import By
def test_bing(browser):

    time.sleep(2)
    order_ele = browser.find_element(By.XPATH, "//div[contains(text(),'FOR_BING')]/../..")
    order_ele.find_elements(By.TAG_NAME, "td")[-1].click()
    time.sleep(4)
    browser.find_element(By.XPATH, "//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/tbody/tr/td[10]/div/div/div/a/mat-icon").click()
    # browser.find_element(By.XPATH, "//mat-icon[data-mat-icon-name='phase_state_enabled']").click()
    time.sleep(50)
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\GO_bing.png")
    assert 'https://www.bing.com/' == browser.find_element(By.XPATH, "//*[@id='screen']/app-aebrs-web-content/div/iframe").get_attribute("src")

if __name__ == '__main__':
    pytest.main(["-s", "test_VS626781.py"])







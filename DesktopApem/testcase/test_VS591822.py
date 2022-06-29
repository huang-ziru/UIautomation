# coding = utf-8
import time
from framework.common import Common
import pytest
from selenium.webdriver.common.by import By
def test_gotoTrack(browser):
    time.sleep(3)
    track = browser.find_elements(by=By.CSS_SELECTOR, value="mat-icon[data-mat-icon-name='double_arrow']")
    Common(browser).eleclick(track[0])
    assert "tracking" in browser.current_url
    browser.find_element(By.CSS_SELECTOR, value="mat-icon[data-mat-icon-name='process_order']").click()
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, value="mat-icon[data-mat-icon-name='tracking']").click()
    assert "tracking" in browser.current_url
if __name__ == '__main__':
    pytest.main(["-s", "test_VS591822.py"])
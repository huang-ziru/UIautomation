# coding = utf-8
from selenium.webdriver import ActionChains
import pytest

def test_warning(browser):
    # mouse = browser.find_element_by_css_selector("mat-icon[svgicon='warning']")
    # ActionChains(browser).move_to_element(mouse).perform()
    # hover_text = browser.find_element_by_xpath("/html/body/div[2]").text
    # assert 'Warning' == hover_text
    # driver.find_element_by_xpath("/html/body/app-root/div/app-sidenav/nav/a[4]").click()
    #Judge whether there is warning or error prompt
    if browser.find_element_by_id("mat-badge-content-0").text != '':
        #get the number of total warnings and errors
        num = browser.find_element_by_id("mat-badge-content-0").text
        browser.find_element_by_css_selector("mat-icon[svgicon='warning']").click()
        #get the number of total text about warnings
        messages = browser.find_elements_by_xpath(("//div[@class='cdk-overlay-pane']/div/mat-list"))
        browser.get_screenshot_as_file(r"..\\report\\result_picture\\warning.png")
        assert num == str(len(messages))
    else:
        browser.find_element_by_css_selector("mat-icon[svgicon='warning']").click()
        message = browser.find_element_by_xpath("//*[@id='cdk-overlay-0']/div/div").get_attribute('textContent')
        browser.get_screenshot_as_file(r"..\\report\\result_picture\\warning.png")
        assert "There is no message." in message

if __name__ == '__main__':
    pytest.main(["-s", "test_VS580601.py"])
    # pytest.main(["--lf", "test_VS580601.py"])


# coding = utf-8

from selenium import webdriver
from framework.basefunc import MainPage
import time, pytest
def test_help(browser):
    try:
        MainPage(browser).is_login_successed()
    except:
        print('Fail:', browser.current_url)
    else:
        # current windows handle
        mainWindow = browser.current_window_handle
        browser.find_element_by_css_selector("mat-icon[svgicon='help']").click()
        # all windows handles
        handles = browser.window_handles
        help_handle = None
        # get the handle of the help page
        for handle in handles:
            if handle != mainWindow:
                help_handle = handle
        # switch to help page
        browser.switch_to.window(help_handle)
        browser.get_screenshot_as_file(r"..\\report\\result_picture\\help.png")
        time.sleep(2)
        try:
            assert 'Help/mobile.htm' in browser.current_url
        except:
            print('fail:', browser.current_url)
        else:
            time.sleep(2)
            #close the page
            browser.close()
            #switch to the order process page
            browser.switch_to.window(mainWindow)
            time.sleep(5)
if __name__ == '__main__':
    pytest.main(["-s", "test_VS580600.py"])
    pytest.main(["--lf", "test_VS580600.py"])

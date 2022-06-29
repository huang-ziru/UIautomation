# coding = utf-8
import time, pytest
from framework.basefunc import MainPage


def test_layout(browser):
    try:
        MainPage(browser).is_login_successed()
    except:
        print('Fail:', browser.current_url)
    else:
        browser.find_element_by_css_selector("mat-icon[data-mat-icon-name='tablet_switch']").click()
        time.sleep(3)
        browser.find_element_by_xpath("//button[@role='menuitem'][2]").click()
        time.sleep(1)
        browser.get_screenshot_as_file(r"..\\report\\result_picture\\desktop.png")
        time.sleep(2)
        try:
            assert "desktop_switch" == browser.find_element_by_xpath("//div[@class='icon'][2]/mat-icon").get_attribute('data-mat-icon-name')
            assert MainPage(browser).is_element_showed("app-sidenav.sidenav") is True

        except:
            print('Switch failed:', browser.find_element_by_xpath("//div[@class='icon'][2]/mat-icon").get_attribute('data-mat-icon-name'))
        else:
            browser.find_element_by_css_selector("mat-icon[data-mat-icon-name='desktop_switch']").click()
            time.sleep(3)
            browser.find_element_by_xpath("//button[@role='menuitem'][1]").click()
            time.sleep(1)
            browser.get_screenshot_as_file(r"..\\report\\result_picture\\tablet.png")
            time.sleep(2)
            assert "tablet_switch" == browser.find_element_by_xpath("//div[@class='icon'][2]/mat-icon").get_attribute('data-mat-icon-name')
            # navgation bar is in the bottom of page
            assert MainPage(browser).is_element_showed("div.mat-tab-link-container") is True

if __name__ == '__main__':
    pytest.main(["-s", "test_VS580603.py"])
    # pytest.main(["--lf", "test_VS580603.py"])



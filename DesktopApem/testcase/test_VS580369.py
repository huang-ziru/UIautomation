# coding = utf-8
import configparser
import time, pytest
from framework.basefunc import MainPage
from selenium.webdriver.common.by import By

def test_fullscreen(browser):
    try:
        MainPage(browser).is_login_successed()
    except:
        print('Fail:', browser.current_url)
    else:
        browser.find_element(By.CSS_SELECTOR, value="mat-icon[svgicon='fullscreen']").click()
        time.sleep(1)
        browser.get_screenshot_as_file(r"..\\report\\result_picture\\fullscreen.png")
        time.sleep(2)
        #get the windows size
        size = browser.get_window_size()
        # get the resolution of the machine that set in the config.ini
        config = configparser.ConfigParser()
        path = r'../framework/config.ini'
        config.read(path)
        width = config.getint('Screen_size', 'width')
        height = config.getint('Screen_size', 'height')
        #assert the size
        assert size["width"] == width
        assert size["height"] == height

        elementObj = browser.find_element(By.XPATH, "/html/body/app-root/app-header")
        browser.execute_script("arguments[0].className='show-header'", elementObj)
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/app-root/app-header/mat-toolbar/div/div[3]/mat-icon[2]").click()
        browser.get_screenshot_as_file(r"..\\report\\result_picture\\exit_fullscreen.png")
        assert browser.get_window_size()["width"] != width
        assert browser.get_window_size()["height"] != height

if __name__ == '__main__':
    pytest.main(["-s", "test_VS580369.py"])
    pytest.main(["--lf", "test_VS580369.py"])
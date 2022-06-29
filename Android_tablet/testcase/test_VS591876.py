# coding = utf-8
import time, pytest
from framework.basefunc import MainPage
from framework.columsfunc import Func

def test_trackscroll(browser):
    try:
        time.sleep(3)
        columns_list = ['checkAuto.', 'checkAssigned WkSt.', 'checkUser Status', 'checkExecuting WkSt.', 'checkExecuting User', 'checkRepetition Count', 'checkUser RUDO', 'checkWkSt. RUDO']
        track = browser.find_elements_by_css_selector("mat-icon[data-mat-icon-name='double_arrow']")
        MainPage(browser).eleclick(track[0])
        time.sleep(3)
        Func(browser).visiblecols(columns_list)
    except:
        print('Fail:', browser.current_url)
    else:
        # top
        js = "var q=document.body.scrollTop=0"
        browser.execute_script(js)
        time.sleep(5)
        # button
        js = "var q=document.body.scrollTop=10000"
        browser.execute_script(js)
        time.sleep(5)
        # scroll into view the designated data
        element = browser.find_element_by_xpath("//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/thead/tr/th[11]")
        browser.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        browser.get_screenshot_as_file(r"..\\report\\result_picture\\trackscroll.png")
        time.sleep(5)



if __name__ == '__main__':
    pytest.main(["-s", "test_VS591876.py"])
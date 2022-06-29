# coding = utf-8
import time, pytest
from framework.basefunc import MainPage
from framework.columsfunc import Func
from selenium.webdriver.common.by import By
def test_scroll(browser):
    try:
        MainPage(browser).is_login_successed()
        visiblecols = ['checkProcess Area', 'checkRep.', 'checkArticle', 'checkPO ', 'checkPO Step', 'checkEnd Date', 'checkProcess Type', 'checkOrigin', 'checkUser Status', 'checkBatch Area', 'checkCR Modified', 'checkRUDO (edit planned)', 'checkRUDO (edit active)', 'checkVer.', 'checkFrom', 'checkSite']
        Func(browser).visiblecols(visiblecols)
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
        element = browser.find_element(By.XPATH, "/html/body/app-root/div/app-process-order/div/div[2]/table/thead/tr/th[21]")
        browser.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        browser.get_screenshot_as_file(r"..\\report\\result_picture\\scoll.png")
        time.sleep(5)



if __name__ == '__main__':
    pytest.main(["-s", "test_VS580580.py"])
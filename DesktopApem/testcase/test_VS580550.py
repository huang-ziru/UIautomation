# coding = utf-8
import time, pytest
from framework.common import Common
from framework.basefunc import MainPage
from framework.columsfunc import Func
from selenium.webdriver.common.by import By
class Testvisiblecols():
    # default columns is showed
    def test_defaultcols(self, browser):
        time.sleep(5)
        assert "Order / Batch Code" == Common(browser).get_text("//*[@id='headerOrder / Batch Code']")
        assert "Quantity" == browser.find_element(By.XPATH, "//*[@id='headerQuantity']").get_attribute('textContent')
        assert "Units" == browser.find_element(By.XPATH, "//*[@id='headerUnits']").get_attribute('textContent')
        assert "Date" == browser.find_element(By.XPATH, "//*[@id='headerDate']").get_attribute('textContent')
        assert "Status" == browser.find_element(By.XPATH, "//*[@id='headerStatus']").get_attribute('textContent')
        assert "Workcenter" == browser.find_element(By.XPATH, "//*[@id='headerWorkcenter']").get_attribute('textContent')
    # selecting all columns and are showed
    def test_visiblecols(self, browser):
        visiblecols = ['checkProcess Area', 'checkRep.', 'checkArticle', 'checkPO ', 'checkPO Step', 'checkEnd Date', 'checkProcess Type', 'checkOrigin', 'checkUser Status', 'checkBatch Area', 'checkCR Modified', 'checkRUDO (edit planned)', 'checkRUDO (edit active)', 'checkVer.', 'checkFrom', 'checkSite']
        Func(browser).visiblecols(visiblecols)
        for id in visiblecols:
            headerid = "header" + id[5::]
            #Scroll to the location where the specified element appears
            target2 = browser.find_element(By.ID, headerid)
            browser.execute_script("arguments[0].scrollIntoView();", target2)
            browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + id + ".png")
            assert id[5::].rstrip() == browser.find_element(By.ID, headerid).text.rstrip()
    # cancle selecting columns and are not showed
    def test_cancelcols(self, browser):
        cancelcols = ['checkQuantity', 'checkUnits', 'checkDate', 'checkStatus', 'checkWorkcenter']
        browser.find_element(By.XPATH, "//*[@id='selectmenu']").click()
        for id in cancelcols:
            path = "//*[@id=\'" + id + "\']/div/mat-pseudo-checkbox"
            time.sleep(2)
            target = browser.find_element(By.ID, id)
            browser.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            if browser.find_element(By.ID, id).get_attribute('aria-selected') == 'true':
                browser.find_element(By.XPATH, path).click()
            time.sleep(1)
        t_element = browser.find_element(By.XPATH, "/html/body/div[2]/div[1]")
        browser.execute_script("arguments[0].click();", t_element)
        time.sleep(5)
        for id in cancelcols:
            headerid = "header" + id[5::]
            browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + id + ".png")
            time.sleep(2)
            assert MainPage(browser).is_element_showed("#" + headerid) is False
        # restore data
        Func(browser).visiblecols(cancelcols)


if __name__ == '__main__':
    pytest.main(["-s", "test_VS580550.py"])



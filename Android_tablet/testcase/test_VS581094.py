# coding = utf-8

from selenium import webdriver
import time, pytest
from framework.basefunc import MainPage
from framework.columsfunc import Func
class Testvisiblecols():
    # default columns is showed
    def test_defaultcols(self, browser):
        assert "Order / Batch Code" == browser.find_element_by_xpath("//*[@id='headerOrder / Batch Code']").text
        assert "Quantity" == browser.find_element_by_xpath("//*[@id='headerQuantity']").text
        assert "Units" == browser.find_element_by_xpath("//*[@id='headerUnits']").text
        assert "Date" == browser.find_element_by_xpath("//*[@id='headerDate']").text
        assert "Status" == browser.find_element_by_xpath("//*[@id='headerStatus']").text
        assert "Workcenter" == browser.find_element_by_xpath("//*[@id='headerWorkcenter']").text
    # selecting all columns and are showed
    def test_visiblecols(self, browser):
        visiblecols = ['checkProcess Area', 'checkRep.', 'checkArticle', 'checkPO ', 'checkPO Step', 'checkEnd Date', 'checkProcess Type', 'checkOrigin', 'checkUser Status', 'checkBatch Area', 'checkCR Modified', 'checkRUDO (edit planned)', 'checkRUDO (edit active)', 'checkVer.', 'checkFrom', 'checkSite']
        Func(browser).visiblecols(visiblecols)
        for id in visiblecols:
            headerid = "header" + id[5::]
            #Scroll to the location where the specified element appears
            target2 = browser.find_element_by_id(headerid)
            browser.execute_script("arguments[0].scrollIntoView();", target2)
            browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + id + ".png")
            assert id[5::].rstrip() == browser.find_element_by_id(headerid).text.rstrip()
    # cancle selecting columns and are not showed
    def test_cancelcols(self, browser):
        cancelcols = ['checkQuantity', 'checkUnits', 'checkDate', 'checkStatus', 'checkWorkcenter']
        Func(browser).visiblecols(cancelcols)
        for id in cancelcols:
            headerid = "header" + id[5::]
            browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + id + ".png")
            time.sleep(2)
            assert MainPage(browser).is_element_showed("#" + headerid) is False


if __name__ == '__main__':
    pytest.main(["-s", "test_VS581094.py"])



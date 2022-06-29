# coding = utf-8
import configparser
import time
from logging import Logger
from selenium import webdriver
from framework.columsfunc import Func
from framework.basefunc import BasePage
'''Data processing '''
class prepare(BasePage):
    #process columns data before the testcase about columns
    def login_after(self):
        # cancle the default status filter
        Func(self.driver).clear_Status()
        # show all columns
        box = ['checkProcess Area', 'checkRep.', 'checkArticle', 'checkPO ', 'checkPO Step', 'checkEnd Date',
               'checkProcess Type', 'checkOrigin', 'checkUser Status', 'checkBatch Area', 'checkCR Modified',
               'checkRUDO (edit planned)', 'checkRUDO (edit active)', 'checkVer.', 'checkFrom', 'checkSite']
        assert 'Order / Batch Code' not in box
        self.driver.find_element_by_xpath("//*[@id='selectmenu']").click()
        for id in box:
            path = "//*[@id=\'" + id + "\']/div/mat-pseudo-checkbox"
            # print(path)
            target = self.driver.find_element_by_id(id)
            self.driver.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            self.driver.find_element_by_xpath(path).click()
            time.sleep(1)
        back = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]")
        self.driver.execute_script("arguments[0].click();", back)
        time.sleep(5)
def login():
    global driver
    desire_cap = {
        "platformName": "Android",
        "platformVersion": "10",
        "deviceName": "6NDNU21227202702",
        "noReset": "true",
        "browserName": "Chrome",
        "forceMjsonwp": "true",
        "chromedriverExecutable": r"F:\Python\Lib\site-packages\appium\webdriver\chromedriver.exe",
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
    time.sleep(5)
    config = configparser.ConfigParser()
    path = r'..\framework\config.ini'
    # open the config.ini and get the data
    config.read(path)
    servername = config.get('login', 'servername')
    username = config.get('login', 'username')
    password = config.get('login', 'password')
    login_alter = username[5::] + ":" + password + "@"
    url = "http://" + login_alter + servername + ".qae.aspentech.com/ApemMobile/#/login"
    driver.get(url)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="mat-input-1"]').send_keys(password)
    driver.find_element_by_id('signInBtn').click()
    time.sleep(6)
    return driver

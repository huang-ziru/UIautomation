# coding = utf-8
import configparser
import time
import re
from logging import Logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from framework.basefunc import BasePage
from selenium.webdriver.common.by import By
'''Data processing '''
class prepare(BasePage):
    #process columns data before the testcase about columns
    def login_after(self):
        # cancle the default status filter
        target = self.driver.find_element(By.XPATH, "//app-filter-box[@id='filterLOGIC_STATUS']/mat-icon")
        self.driver.execute_script("arguments[0].click();", target)
        time.sleep(2)
        self.driver.find_element(By.ID, "mat-checkbox-1").click()
        element = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        # show all columns
        box = ['checkProcess Area', 'checkRep.', 'checkArticle', 'checkPO ', 'checkPO Step', 'checkEnd Date',
               'checkProcess Type', 'checkOrigin', 'checkUser Status', 'checkBatch Area', 'checkCR Modified',
               'checkRUDO (edit planned)', 'checkRUDO (edit active)', 'checkVer.', 'checkFrom', 'checkSite']
        assert 'Order / Batch Code' not in box
        self.driver.find_element(By.XPATH, "//*[@id='selectmenu']").click()
        for id in box:
            path = "//*[@id=\'" + id + "\']/div/mat-pseudo-checkbox"
            # print(path)
            target = self.driver.find_element(By.ID, id)
            self.driver.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            target = self.driver.find_element(By.XPATH, path)
            self.driver.execute_script("arguments[0].click();", target)
            time.sleep(1)
        element = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(5)
def login():
    global driver
    config = configparser.ConfigParser()
    path = r'..\framework\config.ini'
    # open the config.ini and get the data
    config.read(path)
    browser_name = config.get('Browser', 'browser')
    if browser_name == 'Chrome':
        s = Service(r'..\framework\chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        driver.maximize_window()
    elif browser_name == 'Edge':
        driver = webdriver.Edge(r'..\framework\msedgedriver.exe')
        driver.maximize_window()
    else:
        Logger.error('Do not support the Browser')
    servername = config.get('login', 'servername')
    username = config.get('login', 'username')
    loginname =re.split(r'\\', username)[1]
    password = config.get('login', 'password')
    login_alter = loginname + ":" + password + "@"
    url = "http://" + login_alter + servername + "/ApemMobile/#/login"
    driver.get(url)
    time.sleep(30)
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="mat-input-1"]').send_keys(password)
    time.sleep(6)
    driver.find_element(By.ID, 'signInBtn').click()
    time.sleep(30)
    return driver


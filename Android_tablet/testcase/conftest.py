import os, sys
from logging import Logger
import configparser
import time
from appium import webdriver
import pytest
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
@pytest.fixture()
def browser():
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
    time.sleep(5)
    yield driver
    time.sleep(5)
    driver.quit()
    return driver



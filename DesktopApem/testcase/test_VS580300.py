import configparser, os
from logging import Logger
import re
from selenium import webdriver
import time, pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
def login(name, password1, caseID):
    global driver
    config = configparser.ConfigParser()
    dirname = os.path.dirname(os.path.abspath(__file__))
    path = dirname + '/../framework/config.ini'
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
    time.sleep(60)
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(name)
    driver.find_element(By.XPATH, '//*[@id="mat-input-1"]').send_keys(password1)
    driver.find_element(By.ID, 'signInBtn').click()
    time.sleep(60)
    now_url = driver.current_url
    driver.get_screenshot_as_file(r"..\\report\\result_picture\\" + caseID + ".png")
    # print('nowurl:', now_url)
    if now_url != url:
        text1 = driver.current_url
    elif now_url == url:
        text1 = driver.find_element(By.XPATH, '/html/body/app-root/div/app-login/div/div[1]/form/div').text
    else:
        return 'warning！'
    driver.quit()
    return text1

# login with legal username and password
def test_loginok():
    assert "process-order" in login('apem-c-d7\\administrator', 'Aspen100','580300')

# login with username and password without domain name
def test_nodomain():
    assert "WinNTUserNoDomain" in login('hahahha', 'hdhdhhdhd', 'nodomain')

def test_login_ui():
    global driver
    config = configparser.ConfigParser()
    dirname = os.path.dirname(os.path.abspath(__file__))
    path = dirname + '/../framework/config.ini'
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
    sign_in = driver.find_element(By.ID, 'signInBtn')
    driver.get_screenshot_as_file(r"..\\report\\result_picture\\noinput.png")
    time.sleep(30)
    #"Sign in" button is grey out befor input username and password
    assert sign_in.get_attribute('disabled') == 'true'
    assert sign_in.value_of_css_property('background-color') == 'rgba(0, 0, 0, 0.12)'
    #"Eye" icon is shown at the rightmost when typing the password, and user can see the typed when hold it
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('hshhsh')
    driver.find_element(By.XPATH, '//*[@id="mat-input-1"]').send_keys('hhhhhhhhyywywy')
    driver.find_element(By.XPATH, "/html/body/app-root/div/app-login/div/div[1]/form/mat-form-field[2]/div/div[1]/div[4]/mat-icon").click()
    time.sleep(30)

    assert driver.find_element(By.XPATH, '//*[@id="mat-input-1"]').get_attribute("type") == 'text'
    assert sign_in.value_of_css_property('background-color') == 'rgba(38, 152, 251, 1)'
    driver.get_screenshot_as_file(r"..\\report\\result_picture\\input.png")
    driver.quit()

if __name__ == '__main__':
    pytest.main(["-s", "test_VS580300.py"])
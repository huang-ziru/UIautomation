# coding = utf-8
import datetime
import json
import re
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    #assert if login successfully
    def is_login_successed(self):
        if "process-order" in self.driver.current_url:
            return True
        else:
            print("login failed!The url is '%s'"%self.driver.current_url)
            return False
        # the existence of an element is judged by its length
    def is_element_showed(self, css):
        lenth = self.driver.find_elements_by_css_selector(css_selector=css)
        if len(lenth) == 0:
            return False
        else:
            return True
        # get the data from config.ini
    def get_configdata(self):
        with open('E:/PycharmProjects/ApemMobile/framework/config.json', 'r', encoding='utf8')as fp:
            json_data = json.load(fp)
        return json_data
    #logout click
    def logout(self):
        self.driver.find_element_by_xpath("/html/body/app-root/app-header/mat-toolbar/div/div[5]/mat-icon").click()
        time.sleep(5)
        logout_button = self.driver.find_element_by_xpath('//*[@id="logoutpanel"]/button[2]')
        logout_button.click()
    # get the table element except table head
    def get_table(self, x):
        # get the row elements
        table_tr_list = self.driver.find_elements_by_xpath("//div[@class='full show-navigation']/div[2]/table/tbody/tr")
        table_list = []
        for tr in table_tr_list:
            # except circle column
            table_td_list = tr.find_elements_by_tag_name("td")[x::]
            row_list = []
            for td in table_td_list:
                row_list.append(td.text)
            table_list.append(row_list)
        return table_list
    #get the table columns data
    def td_data(self, td_list):
        td_data_list = []
        if td_list == []:
            td_data_list.append('')
        else:
            for i in range(len(td_list)):
                td_text = td_list[i].text
                if 'PHASE' in td_text:
                    text_list = td_text.split('\n')
                    td_data_list.append(text_list[0])
                else:
                    td_data_list.append(td_text)
        return td_data_list
    #handle order data to get ordername
    def table_ordername(self, td_list):
        order_namelist = []
        for i in range(len(td_list)):
            # Match extraction ordername
            name = re.split(r'/', td_list[i])[0]
            order_namelist.append(name)
        return order_namelist
    #handle date columns,type from string to date
    def datetime_str(self, str_time):
        if 'M' in str_time:
            str_timelist = str_time.split(',')
            dateTime_p = datetime.datetime.strptime(str_timelist[0], '%m/%d/%y')
            #date is null
        elif str_time == '':
            dateTime_p = datetime.datetime.strptime('01/01/1000', '%m/%d/%Y')
        else:
            date_str=re.split(r'/', str_time)
            if len(date_str[2]) == 2:
                dateTime_p = datetime.datetime.strptime(str_time, '%m/%d/%y')
            else:
                dateTime_p = datetime.datetime.strptime(str_time, '%m/%d/%Y')
        return dateTime_p
    # get the sorting rule,ascend or descend
    def get_revers(self, head_ele):
        target = head_ele.find_elements_by_tag_name("div")[2]
        self.driver.execute_script("arguments[0].click();", target)
        revers = head_ele.get_attribute('aria-sort')
        return revers
    #clear the input data in number filters
    def clear_input(self, ele, inputpath1, inputpath2):
        target = ele.find_element_by_tag_name("mat-icon")
        self.driver.execute_script("arguments[0].click();", target)
        self.driver.find_element_by_xpath(inputpath1)
        target1 = self.driver.find_element_by_xpath(inputpath1)
        self.driver.execute_script("arguments[0].click();", target1)
        #Press<Ctrl+a>,then press <Delete>
        self.driver.find_element_by_xpath(inputpath1).send_keys(Keys.CONTROL, "a")
        time.sleep(1)
        self.driver.find_element_by_xpath(inputpath1).send_keys(Keys.DELETE)
        time.sleep(1)
        target2 = self.driver.find_element_by_xpath(inputpath2)
        self.driver.execute_script("arguments[0].click();", target2)
        self.driver.find_element_by_xpath(inputpath2).send_keys(Keys.CONTROL, "a")
        time.sleep(1)
        self.driver.find_element_by_xpath(inputpath2).send_keys(Keys.DELETE)
        time.sleep(1)
        target = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]")
        self.driver.execute_script("arguments[0].click();", target)
    # get the table head element
    def get_tablehead(self):
        #except circle and tracking
        table_head_list = self.driver.find_elements_by_xpath("//div[@class='full show-navigation']/div[2]/table/thead/tr/th")[1:-1:]
        return table_head_list
    def navigate(self, ele_path):
        elementObj = self.driver.find_element_by_xpath("/html/body/app-root/div/app-navigation")
        self.driver.execute_script("arguments[0].className='show-nav'", elementObj)
        nav_text = self.driver.find_element_by_xpath(ele_path).get_attribute("textContent")
        return nav_text
    def dateSort(self,str_time):
        if 'M' in str_time:
            dateTime_p = datetime.datetime.strptime(str_time, '%m/%d/%y, %I:%M:%S %p')
            # date is null
        elif str_time == '':
            dateTime_p = datetime.datetime.strptime('01/01/1000, 01:01:01 am', '%m/%d/%Y, %I:%M:%S %p')
        else:
            str_time = str_time + ", 01:01:00 am"
            date_str = re.split(r',', str_time)
            date_s = re.split(r'/', date_str[0])
            if len(date_s[2]) == 2:
                dateTime_p = datetime.datetime.strptime(str_time, '%m/%d/%y, %I:%M:%S %p')
            else:
                dateTime_p = datetime.datetime.strptime(str_time, '%m/%d/%Y, %I:%M:%S %p')
        return dateTime_p
    def eleclick(self,ele):
        try:
            ele.click()
        except:
            self.driver.execute_script("arguments[0].click();", ele)
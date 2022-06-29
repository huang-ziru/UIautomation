# coding = utf-8
import datetime
import re
from selenium.webdriver import ActionChains
from framework.basefunc import BasePage
from selenium.webdriver.common.by import By

class Common(BasePage):
    # get the table element except table head
    def get_table(self, x):
        #get the row elements
        table_tr_list = self.driver.find_elements(By.XPATH, "//div[@class='full show-navigation']/div[2]/table/tbody/tr")
        table_list = []
        for tr in table_tr_list:
            #except circle column
            table_td_list = tr.find_elements(By.TAG_NAME, "td")[x::]
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
            #Match extraction ordername
            name_batch = re.split(r'/', td_list[i])[0]
            name = re.split(r'\n', name_batch)[0]
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
        target = head_ele.find_elements(By.TAG_NAME, "div")[2]
        self.driver.execute_script("arguments[0].click();", target)
        revers = head_ele.get_attribute('aria-sort')
        return revers

    # get the table head element
    def get_tablehead(self):
        #except circle and tracking
        table_head_list = self.driver.find_elements(By.XPATH, "//div[@class='full show-navigation']/div[2]/table/thead/tr/th")[1:-1:]
        return table_head_list
    def navigate(self, ele_path):
        elementObj = self.driver.find_element(By.XPATH, "/html/body/app-root/div/app-sidenav")
        mouse = elementObj.find_element(By.XPATH, ele_path)
        ActionChains(self.driver).move_to_element(mouse).perform()
        nav_text = self.driver.find_element(By.CSS_SELECTOR, value="div.cdk-overlay-container>div>div>mat-tooltip-component>div").text
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
    def get_text(self,xpath):
        ele = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].click();", ele)
        text = ele.get_attribute('textContent')
        return text
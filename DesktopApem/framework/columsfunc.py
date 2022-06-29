# coding = utf-8
from framework.basefunc import BasePage
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class Func(BasePage):
    # clear columns status default filter
    def clear_Status(self):
        target = self.driver.find_element(By.XPATH, "//app-filter-box[@id='filterLOGIC_STATUS']/mat-icon")
        self.driver.execute_script("arguments[0].click();", target)
        time.sleep(2)
        select_all = self.driver.find_element(By.XPATH, "//mat-selection-list/section[1]/mat-checkbox/label/div/input")
        self.driver.execute_script("arguments[0].click();", select_all)
        element = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
    # visible columns select
    def visiblecols(self, visiblecols):
        self.driver.find_element(By.XPATH, "//*[@id='selectmenu']").click()
        for id in visiblecols:
            path = "//*[@id=\'" + id + "\']/div/mat-pseudo-checkbox"
            time.sleep(2)
            target = self.driver.find_element(By.ID, id)
            self.driver.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            if self.driver.find_element(By.ID, id).get_attribute('aria-selected') == 'false':
                self.driver.find_element(By.XPATH, path).click()
            time.sleep(1)
        element = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(5)
    # mouse hover to get text
    def hover_text(self, xpath):
        mouse = self.driver.find_element(By.XPATH, xpath)
        ActionChains(self.driver).move_to_element(mouse).perform()
        hover_text = self.driver.find_element(By.XPATH, "/html/body/div[2]").text
        return hover_text
    def cancelecols(self, visiblecols):
        self.driver.find_element(By.XPATH, "//*[@id='selectmenu']").click()
        for id in visiblecols:
            path = "//*[@id=\'" + id + "\']/div/mat-pseudo-checkbox"
            time.sleep(2)
            target = self.driver.find_element(By.ID, id)
            self.driver.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            if self.driver.find_element(By.ID, id).get_attribute('aria-selected') == 'true':
                self.driver.find_element(By.XPATH, path).click()
            time.sleep(1)
        element = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(5)





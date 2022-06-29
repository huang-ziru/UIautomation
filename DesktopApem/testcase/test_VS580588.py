# coding = utf-8
import time
import re, pytest
from selenium.webdriver.common.by import By

class Testsearch():
    def test_search(self, browser):
        #search with key_words 'er'
        browser.find_element(By.ID, "ordersearch").send_keys('order')
        time.sleep(2)
        browser.get_screenshot_as_file(r"..\\report\\result_picture\\search.png")
        table_list = []
        table_tr_list = browser.find_elements(By.XPATH, "//div[@class='full show-navigation']/div[2]/table/tbody/tr")
        # match 'er' and case insensitive
        pattern = re.compile(r'order', re.I)
        count1 = 0
        for tr in table_tr_list:
            table_td_list = tr.find_elements(By.TAG_NAME, "td")[1::]
            for td in table_td_list:
                row_list = []
                row_list.append(td.text)
                table_list.append(row_list)
                #Verify bold matches
                strong_list = td.find_elements(By.TAG_NAME, "strong")
                for st in strong_list:
                    count1 = count1 + 1
                    result1 = re.sub(pattern, '', st.text)
                    assert len(result1) == 0
        #Verify that there are matches in the non BOLD data
        count2 = 0
        for i in range(len(table_list)):
            for j in range(len(table_list[i])):
                it = re.finditer(pattern, table_list[i][j])
                for ww in it:
                    count2 = count2 + 1

        assert count1 == count2
        time.sleep(5)

if __name__ == '__main__':
    pytest.main(["-s", "test_VS580588.py"])






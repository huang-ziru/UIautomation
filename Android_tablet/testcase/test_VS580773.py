import time
import pytest
from framework.basefunc import MainPage
class Testnavigate():
    def test_order(self, browser):
        assert 'Process Order' in MainPage(browser).navigate("//app-navigation/nav/div[2]/div/div/a[1]/div")

    def test_tracking(self, browser):
        assert 'Tracking' == MainPage(browser).navigate("//mat-icon[@data-mat-icon-name='process_order']/../following-sibling::a[1]/div")

    def test_setting(self, browser):
        assert 'Settings' == MainPage(browser).navigate("//mat-icon[@data-mat-icon-name='process_order']/../following-sibling::a[2]/div")

    def test_autohide(self, browser):
        browser.find_element_by_xpath("/html/body/app-root/div/div").click()
        assert MainPage(browser).is_element_showed("app-navigation.show-nav") is True
        time.sleep(5)
        assert MainPage(browser).is_element_showed("app-navigation.hide-nav") is True




if __name__ == '__main__':
    pytest.main(["-s", "test_VS580773.py"])


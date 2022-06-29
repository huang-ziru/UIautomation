# coding = utf-8
import pytest
from framework.basefunc import MainPage
class Testtitle_bar():
    def test_userinfo(self, browser):
        assert MainPage(browser).is_element_showed(css="mat-icon[svgicon='account']") is True

    def test_help(self, browser):
        assert MainPage(browser).is_element_showed(css="mat-icon[svgicon='help']") is True

    def test_fullscreen(self, browser):
        assert MainPage(browser).is_element_showed(css="mat-icon[svgicon='fullscreen']") is True

    def test_desktop_switch(self, browser):
        assert MainPage(browser).is_element_showed(css="mat-icon[data-mat-icon-name='desktop_switch']") is True

    def test_warning(self, browser):
        assert MainPage(browser).is_element_showed(css="mat-icon[svgicon='warning']") is True

if __name__ == '__main__':
    pytest.main(["-s", "test_VS580358.py"])


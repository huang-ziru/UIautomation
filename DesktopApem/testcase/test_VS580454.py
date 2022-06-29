# coding = utf-8
import pytest
from framework.basefunc import MainPage

def test_loading(browser):
    assert MainPage(browser).is_element_showed(css="app-loading.loading") is True

if __name__ == '__main__':
    pytest.main(["-s", "test_VS580454.py"])


# coding = utf-8
import pytest
from framework.common import Common
def test_navigate(browser):

    assert 'Process Order' in Common(browser).navigate("//mat-icon[@data-mat-icon-name='process_order']")
    assert 'Tracking' == Common(browser).navigate("//mat-icon[@data-mat-icon-name='process_order']/../following-sibling::a[1]/mat-icon")
    assert 'Settings' == Common(browser).navigate("//mat-icon[@data-mat-icon-name='process_order']/../following-sibling::a[2]/mat-icon")

if __name__ == '__main__':
    pytest.main(["-s", "test_VS580450.py"])


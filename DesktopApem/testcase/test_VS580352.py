# coding = utf-8
import pytest
from testcase.test_VS580300 import login

# login with username and password without access
def test_Denied():
    assert "You do not have permission to login." in login('corp\\qaone', 'Aspen111','580352')

if __name__ == '__main__':
    pytest.main(["-s", "test_VS580352.py"])
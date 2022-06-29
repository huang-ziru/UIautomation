# coding = utf-8
import pytest
from testcase.test_VS580300 import login

# login with invalid username and password
def test_Invalid():
    assert "Invalid username or password. Please re-enter domain\\username and password." in login('jhh\\hahahha', 'hdhdhhdhd','580320')

if __name__ == '__main__':
    pytest.main(["-s", "test_VS580320.py"])
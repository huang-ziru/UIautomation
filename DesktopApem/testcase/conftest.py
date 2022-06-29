import os, sys
import pytest
from framework.Login import login
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
@pytest.fixture()
def browser():
    '''Define global driver parameters'''
    driver = login()
    yield driver
    driver.quit()
    return driver


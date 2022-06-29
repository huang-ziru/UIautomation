import configparser
import os
local_path = os.path.split(os.path.realpath(__file__))[0]
configfile = local_path+r'\config.ini'
def ReadConfig(section, name):
    cf = configparser.ConfigParser()
    cf.read(configfile)
    readresult=cf.get(section, name)
    return readresult

SupportBrowser = {
    'Browser': ReadConfig('Browser', 'browser')
}

LoginModel = {
    "ServerName": ReadConfig('login', 'servername'),
    "UserName": ReadConfig('login', 'username'),
    "PassWord": ReadConfig('login', 'password')
}

AssertValue = {
    'Workstation': ReadConfig('login', 'workstation'),
    "Width": ReadConfig('Screen_size', 'width'),
    "height": ReadConfig('Screen_size', 'width')
}
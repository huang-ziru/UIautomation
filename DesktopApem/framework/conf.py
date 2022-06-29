#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xml.etree.ElementTree as ET
import configparser
#import socket
def conf_xml():
    xml = "C:\\Program Files\\Common Files\\AspenTech Shared\\Tomcat9.0.27\\webapps\\ApemMobile\\WEB-INF\\web.xml"
    tree = ET.parse(xml)
    root = tree.getroot()
    conf = []
    count = 0
    for init in root.findall('servlet'):
        for value in init.findall('init-param'):
            count = count + 1
            if count == 4:
                value[1].text = 'false'
            conf.append(value[1].text)
    tree.write(xml, encoding='utf-8')
#def modifyConf():
#    Compute_name = socket.getfqdn()
#    sever_name = socket.gethostname()
#    fixConfig = configparser.ConfigParser()
 #   fixConfig.read('framework/config.ini')
#    fixConfig.set("login", "servername", sever_name)
#    fixConfig.set("login", "workstation", Compute_name)
#    fixConfig.write(open('framework/config.ini', "r+"))





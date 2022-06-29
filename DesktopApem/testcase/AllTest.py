import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("DesktopApem\\")+len("DesktopApem\\")]
sys.path.extend([rootPath, rootPath])
from xml.dom.minidom import parse
from xml.dom.minidom import Document
from framework.conf import conf_xml
#from framework.conf import modifyConf
conf_xml()
#modifyConf()
# Process the current script running address
path1 = os.path.dirname(os.path.abspath(__file__))
# command = "pytest " + path1 + " --junit-xml=../report/report1.xml"
# os.system(command)
import xml.dom.minidom
import re
DOMTree = xml.dom.minidom.parse("..\\report\\report1.xml")
collection = DOMTree.documentElement
testsuite = collection.getElementsByTagName("testsuite")
if testsuite[0].getAttribute("failures") != '0':
    command = "pytest --lf " + path1 + " --junit-xml=../report/report2.xml"
    os.system(command)

#Create a document object
doc = Document()
#Create a root node
root = doc.createElement('testsuites')
#Join root node to tree
doc.appendChild(root)
#Create secondary node
testsuite = doc.createElement('testsuite')
testresult = doc.createElement('testresult')
# Using minidom parser to open XML document
filename = path1 + '\..\\report\\report2.xml'
DOMTree = xml.dom.minidom.parse("..\\report\\report1.xml")
collection = DOMTree.documentElement
CaseNames_fail = []
if os.path.exists(filename) is True:
    DOMTree2 = xml.dom.minidom.parse(filename)
    collection2 = DOMTree2.documentElement
    testsuites = collection2.getElementsByTagName("testsuite")
    num_failed = testsuites[0].getAttribute("failures")
    testcases = collection2.getElementsByTagName("testcase")
    for testcase in testcases:
        classname = testcase.getAttribute("classname")
        casename = testcase.getAttribute("name")
        case_id = classname.split('.')[0]
        failure = testcase.getElementsByTagName('failure')
        if failure != []:
            message = failure[0].getAttribute('message')
            casepoint = doc.createElement('testcase')
            casepoint.setAttribute('result', 'failed')
            casepoint.setAttribute('case_id', case_id)
            casepoint.setAttribute('case_name', casename)
            casepoint.setAttribute('message', message)
            vsts_id = 'VSTS' + re.sub(r'\D', "", case_id)
            casepoint.setAttribute('VSTS_id', vsts_id)
            testresult.appendChild(casepoint)
            if casename not in CaseNames_fail:
                CaseNames_fail.append(casename)
else:
    testsuites = collection.getElementsByTagName("testsuite")
    num_failed = testsuites[0].getAttribute("failures")
testcases = collection.getElementsByTagName("testcase")
for testcase in testcases:
    classname = testcase.getAttribute("classname")
    casename = testcase.getAttribute("name")
    case_id = classname.split('.')[0]
    if casename not in CaseNames_fail:
        casepoint = doc.createElement('testcase')
        casepoint.setAttribute('result', 'passed')
        casepoint.setAttribute('case_id', case_id)
        casepoint.setAttribute('case_name', casename)
        vsts_id = 'VSTS' + re.sub(r'\D', "", case_id)
        casepoint.setAttribute('VSTS_id', vsts_id)
        testresult.appendChild(casepoint)
        testsuite.appendChild(testresult)
        root.appendChild(testsuite)
testsuites = collection.getElementsByTagName("testsuite")
total_test = testsuites[0].getAttribute("tests")
error = testsuites[0].getAttribute("errors")
skipped = testsuites[0].getAttribute("skipped")
time = testsuites[0].getAttribute("time")
num_passed = int(total_test) - int(num_failed)
testsuite.setAttribute('errors', error)
testsuite.setAttribute('failed', str(num_failed))
testsuite.setAttribute('skipped', skipped)
testsuite.setAttribute('passed', str(num_passed))
testsuite.setAttribute('total', total_test)
testsuite.setAttribute('time', time)

#存成xml文件
fp = open('..\\report\\test.xml','w',encoding='utf-8')
doc.writexml(fp, indent='', addindent='\t', newl='\n', encoding='utf-8')
fp.close()


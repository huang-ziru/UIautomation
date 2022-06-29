import os
os.system('pytest -q -s ..\\testcase --html=../report/result1.html')
from lxml import etree
f = open("../report/result1.html", "r", encoding="utf-8")
#Convert file content to string
file = f.read()
#Convert a string to a processable format
html = etree.HTML(file)
result_list = html.xpath("//td[contains(@class,'col-result')]")
# print(result_list)
Failed_testcase = []
for result in result_list:
    # print(result.xpath("text()"))
    if result.xpath("text()") == ['Failed']:
        testcaseID = result.xpath('../td[@class="col-name"]/text()')[0].split('::')[0]
        if testcaseID not in Failed_testcase:
            Failed_testcase.append(testcaseID)
if len(Failed_testcase) != 0:
    os.system('pytest --lf ..\\testcase --html=../report/result2.html')




# -*- coding:utf-8 -*-
import unittest
from testcase import createNewTest
import HTMLTestRunner
if __name__ == '__main__':
    suit=unittest.TestSuite()
    suit.addTest(createNewTest.CreateTest("test_addOk"))
    suit.addTest(createNewTest.CreateTest("test_addIdIsNull"))
    suit.addTest(createNewTest.CreateTest("test_addUseridIsNull"))
    # runner=unittest.TextTestRunner()
    # runner.run(suit)
    file=open("report/testReport.html",'wb')
    runner=HTMLTestRunner.HTMLTestRunner(file,title=u"接口测试",description=u"test")
    runner.run(suit)
   
#删除的接口 unittest 写测试用例
#生成测试报告

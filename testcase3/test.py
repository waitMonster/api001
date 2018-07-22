# -*- coding:utf-8 -*-
import unittest

if __name__ == '__main__':
    #unittest.main()
    # 实例化测试套件
    suite = unittest.TestSuite()
    # 将测试用例加载到测试套件中
    # 行顺序是安装加载顺序：
    suite.addTest(weatherTest('test01'))
    #suite.addTest(weatherTest('test02'))
    #suite.addTest(Test1('test_One'))
# 实例化TextTestRunner类
# 使用run()方法运行测试套件（即运行测试套件中的所有用例）
    runner = unittest.TextTestRunner()
    runner.run(suite)
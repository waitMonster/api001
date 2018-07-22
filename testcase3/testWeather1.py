# -*- coding:utf-8 -*-
import requests
import unittest
#     url='https://www.sojson.com/open/api/weather/json.shtml'
#     data={'city':'北京'}
#     res=requests.get(url,data)
#     print(res.text)
class weatherTest(unittest.TestCase):
    def test01(self):
        url='https://www.sojson.com/open/api/weather/json.shtml'
        data={'city':'北京'}
        res=requests.get(url,data)
        print(res.text)
        resObj=res.json()
        self.assertEqual(resObj['city'],u"北京")
        self.assertEqual(len(resObj['data']['forecast']),5)
        self.assertEqual(resObj['data']['forecast'][0]['type'], u"雷阵雨")
    def test02(self):
        url='https://www.sojson.com/open/api/weather/json.shtml'
        data={'city':'杭州'}
        res=requests.get(url,data)
        print(res.text)
        resObj=res.json()
        self.assertEqual(resObj['city'],"杭州")
    # def test03(self):
    #     url='https://www.sojson.com/open/api/weather/json.shtml'
    #     data={'city':''}
    #     res=requests.get(url,data)
    #     print(res.text)
    #     resObj=res.json()
    #     self.assertEqual(resObj['status'],400)


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
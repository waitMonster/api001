# -*- coding:utf-8 -*-
import xlrd
import json
from Api.HttpApi import *
from Api.excelApi import *
#1.把从第一行开始，把每一行的数据转换成字段的形式，key值是我们对应的第一行的值
#2.将所有的这些字典转换为list[{"url":"","参数":""},{"url":"","参数":""}]
#3.把excel中数据  调用我们的post接口  进行接口测试
#分装方法的步骤
#1.方法，写成流水账形式
#2 方法样式加上 def xxxx():
#3. return 返回值
#4寻找通用变量，然后用参数替换
#5把我们的方法，放到其他的文件中，方便所有的人调用
#6，新建一个类,类中的方法 要加self
#7 调用方法，实例化，实例化后调用中的方法

    #print http.send_post(disc[u"接口地址"],json.dumps(json.loads(disc[u"参数"])))
#print(json.dumps(dataList).decode("unicode-escape"))
#print(dataList[0])

#----------------------
if __name__ == '__main__':
    excelApi=excelApi()
    dataList=excelApi.excelRead("..\data\TestCase.xlsx")
    print(dataList)
    url=dataList[0][u"接口地址"]
    data=json.dumps(json.loads(dataList[0][u"参数"]))
    # print(type(url))
    # print(type(data))
    # print http.send_post(url,data)
    http=HttpApi()
    for dataValues in dataList:
        url = dataValues[u"接口地址"]
        data = json.dumps(json.loads(dataValues[u"参数"]))
        print  http.send_post(url,data)
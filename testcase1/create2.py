# -*- coding:utf-8 -*-
import json
from Api.HttpApi import HttpApi
import requests
if __name__ == '__main__':
    #获取参数数据
    f=open('../data/create.json')
    data=json.load(f)
    f.close()
    data1=json.dumps(data)
    print(data)
    newdata=data1.replace('ID','80')
    newdata1=newdata.replace('usersId','80')
    print(newdata1)
    #定义url
    url='http://47.92.88.246:8999/it-license/it/license/create'
    #实例化
    # http=httpapi()
    # http.send_post(url,data)
    print type(data1)
    headers = {'content-type': 'application/json'}
    # res=requests.post(url=url,data=data1,headers=headers)
    # res=requests.post(url=url,json=data,headers=headers)
    # print(res.json())
    http=HttpApi()
    res= http.send_post(url,newdata1,headers)
    print(res)
    print(res['result'])
    #作业2
    #json值有三个变量，封装一个方法，将三个变量替换为新的值
    #  建议传参的方式是 字典类型
    #  提示  用字典的遍历   用replace替换
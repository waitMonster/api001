# -*- coding:utf-8 -*-
import requests
# def he(num1,num2):
#     c = num1 + num2
#     return c
# a=1
# b=1
# print he(a,b)
# print he(num1=a,num2=b)


url='https://www.sojson.com/open/api/weather/json.shtml'
data={'city':"北京"}
res = requests.get(url=url, params=data)
print res.json()

res=requests.get(url=url,params=data)
print res.json()

def send_get(url,data):
    res = requests.get(url=url, params=data)
    return res.json()
#get，url和参数，
#1.顺序去把操作写出来
#2.考虑字段作为传参变量
#3.考虑封装

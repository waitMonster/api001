# -*- coding:utf-8 -*-
import requests
# url='https://www.sojson.com/open/api/weather/json.shtml?city=北京'
# res=requests.get(url)
# city=北京\
url='https://www.sojson.com/open/api/weather/json.shtml'
data={'city':"北京"}
# def
#     res=requests.get(url,data)
#     print(res.text)
#  封装一个函数，参数 城市  ，返回值  该城市的天气信息
#1.获取一个城市天气信息
#2.将城市作为变量
#3.按照需求 封装方法
# def weateher(city):
#     url = 'https://www.sojson.com/open/api/weather/json.shtml'
#     data = {'city': city}
#     res = requests.get(url, data)
#     return res.json()
# print(weateher('北京'))


#封装get方式 参数  url  parama
def send_get(url,params):
    res=requests.get(url=url,params=params)
    return res.json()

# url="http://v.juhe.cn/calendar/day"
# data={"date":"2015-1-1","key":"3fc2053b46fcafdaacd98165f31706d4"}
# resPost=requests.post(url=url,data=data)
# print resPost.text
url='https://www.sojson.com/open/api/weather/json.shtml'
data={'city':"北京"}
print send_get(url,data)
print send_get(params=data,url=url)

# -*- coding:utf-8 -*-
import requests
url='https://www.sojson.com/open/api/weather/json.shtml?city=%E5%8C%97%E4%BA%AC'
res=requests.get(url)
print(res.text)
print(type(res.text))
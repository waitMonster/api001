# -*- coding:utf-8 -*-
import requests
import json
if __name__ == '__main__':

    url = 'http://v.juhe.cn/calendar/day'
    data={"date":"2015-1-1","key":"3fc2053b46fcafdaacd98165f31706d4"}
    # headers = {'content-type': 'application/json'}
    r= requests.post(url,data=data)
    print r.text
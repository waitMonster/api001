# -*- coding:utf-8 -*-
from Api.common import *
from Api.HttpApi import *
import json
if __name__ == '__main__':
    chageData = CommonMethod()
    http = HttpApi()
    url = 'http://47.92.88.246:8999/it-license/it/license/product/version'
    headers = {'content-type': 'application/json'}
    fp = open("..\data\select.json")
    data = json.load(fp)
    change = {}
    change['ID'] = '888'
    change['usersId'] = '666'
    newData=chageData.changeDate(json.dumps(data),change)
    print(newData)
    res=http.send_post(url=url,data=newData,headers=headers)
    print(res)
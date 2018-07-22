# -*- coding:utf-8 -*-
import json
from Api.common import *
from Api.HttpApi import *
from Api.LicesenCommon import *
if __name__ == '__main__':
    #
    chageData=CommonMethod()
    http=HttpApi()
    url='http://47.92.88.246:8999/it-license/it/license/create'
    headers = {'content-type': 'application/json'}
    fp=open("..\data\create.json")
    data=json.load(fp)
    change={}
    change['ID']='888'
    change['usersId']='666'
    newData=chageData.changeDate(json.dumps(data),change)
    print(newData)
    res=http.send_post(url,newData,headers)
    print(res['result'])
    change['DataID']=res['result']
    #删除
    lisen=LicesenMethod()
    lisen.deleteLicesen(change)


# 封装读取json文件的方法
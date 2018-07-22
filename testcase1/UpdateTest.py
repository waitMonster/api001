# -*- coding:utf-8 -*-
from Api.common import *
from Api.HttpApi import *
from Api.LicesenCommon import *
import json
if __name__ == '__main__':
    chageData = CommonMethod()
    http = HttpApi()
    licesen=LicesenMethod()
    change = {}
    change['ID'] = '8'
    change['usersId'] = '666'
    licesenId=licesen.createLicesen(change)
    print(licesenId)

    url = 'http://47.92.88.246:8999/it-license/it/license/update'
    headers = {'content-type': 'application/json'}
    fp = open("..\data\update.json")
    data = json.load(fp)
    change['DataID'] = licesenId
    newData=chageData.changeDate(json.dumps(data),change)
    print(newData)
    res=http.send_post(url=url,data=newData,headers=headers)
    print(res)
# -*- coding:utf-8 -*-
import json
from Api.common import CommonMethod


#json["A1"]='b1'
# print(data)
# data2=json.dumps(data).replace("a1","b1")
# data3=json.dumps(data).replace("a2","b2")

# print(data3)
#1.新建一个字典
#。遍历
#3.取遍历的值
#替换
#a1----b1
#a2----b2
#a3----b3


if __name__ == '__main__':
    changeD = CommonMethod()
    # data = {"A1": "a1", "A2": "a2", "A3": {"A1": "a1", "A2": "a2", "A3": "a3"}}
    # change = {}
    # change['a1'] = 'b1'
    # change['a2'] = 'b2'
    # change['a3'] = 'b3'
    change = {}
    change['ID'] = '800'
    change['usersId'] = '2000'
    print(change)

    fp=open("../data/create.json")
    dateFile=json.load(fp)
    print(dateFile)
    print type(dateFile)
    print changeD.changeDate(json.dumps(dateFile),change)
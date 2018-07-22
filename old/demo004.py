# -*- coding:utf-8 -*-
import json

# json.dump()写文件
# json.load()读文件
#
# json.dumps()list-str
# json.loads()str-list
# data={"date":"2015-1-1","key":"3fc2053b46fcafdaacd98165f31706d4"}
# print type(data)
# print(data)
# data1=json.dumps(data)
# print type(data1)
# print(data1)
# data2=json.loads(data1)
# print type(data2)
# print(data2['key'])
#-----
# 1.打开文件
# 2.读取内容 ---写入内容
# 3.关闭文件
f=open('data/create.json')
print(f)
data3=json.load(f)
print(data3)
print(type(data3))
f.close()
# print(data)
# f1=open('write.json','w')
# json.dump(data,f1)
# f1.close()


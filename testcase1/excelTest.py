# -*- coding:utf-8 -*-
import xlrd
import json
from Api.HttpApi import *
if __name__ == '__main__':
    http=HttpApi()
    table=xlrd.open_workbook("../data/TestCase.xlsx")
   # print(table.sheet_by_index(0))
    sheet=table.sheet_by_name("TestCase")
    #print(table.sheets()[0])
    #拿出行和列的总个数
    print(sheet.ncols)
    print(sheet.nrows)
    #获取某一行和某一列的值
    print(sheet.row_values(0))
    # print(sheet.row_values(0)[0])
    # print(sheet.col_values(0))
    # #获取单元格的值
    # print(sheet.cell_value(1,1))
    # firstRow=sheet.row_values(0)
    # for value in firstRow:
    #     print(value)
    #a=[1,2,3]
    # for i in a:
    #     print i
    # print(len(a))
    #for i in range(len(a)):
    # for i in xrange(len(a)):
    #     print a[i]
    # url=sheet.cell_value(1,0)
    # headers=sheet.cell_value(1,2)
    # data=sheet.cell_value(1,3)
    # print(headers)
    # print(eval(headers))
    # #print(type(json.dumps(headers)))
    # #print(json.loads(str(headers)))
    # #headers = {'content-type': 'application/json'}
    #
    # print http.send_post(url=url,data=data,headers=eval(headers))
    #sheet.cell_value(0,0)
    sheet.cell_value(0, 0)
    nRow=sheet.nrows
    nCol=sheet.ncols
    #firstRow=sheet.row_values(0)
    for row in range(nRow):
        #print(sheet.row_values(row))
        #print(row)
        for col in range(nCol):
            print(str(row)+","+str(col))
            #print(sheet.cell_value(0,col))
            print(sheet.cell_value(0,col)+sheet.cell_value(row,col))

    {"url":""}
    {"参数":""}
    #1.把从第一行开始，把每一行的数据转换成字段的形式，key值是我们对应的第一行的值
    #2.将所有的这些字典转换为list[{"url":"","参数":""},{"url":"","参数":""}]
    #3.把excel中数据  调用我们的post接口  进行接口测试

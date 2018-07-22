# -*- coding:utf-8 -*-
import xlrd
import json
#
excel01 = xlrd.open_workbook("../data/TestCase.xlsx")

sheet = excel01.sheet_by_name("TestCase")
sheet.cell_value()
nRow=sheet.nrows
nCol=sheet.ncols
lists =[]
for row in range(nRow):

    dict={}
    # print(sheet.row_values(row))
    # print(row)
    for col in range(1,nCol):
        # print(str(row)+","+str(col))
        #print(sheet.cell_value(0,col))
        if row == 0:
            print (sheet.cell_value(0, col))
        # else:
        #     print (sheet.cell_value(0,col))+sheet.cell_value(row,col)
        else:
            dict[sheet.cell_value(0,col)] = sheet.cell_value(row,col)

    #print json.dumps(dict).decode("unicode-escape")
    lists.append(dict)
print json.dumps(lists).decode("unicode-escape")
#!/usr/bin/python
# -*- coding: utf-8 -*-
from openpyxl import load_workbook
from openpyxl import Workbook
from os import listdir
from os.path import isfile, isdir, join
import re


def findImg(re_rule, files):
    i = 0
    while i < len(files) :
        isFound = False
        match_object = re.match(re_rule, files[i], re.IGNORECASE)
        if match_object != None:
               print(match_object)
               isFound = True
               break
        i +=1
    if isFound == False :
        print('------------'+ re_rule + ' not found -------------')
        return False
    return True

# init excel to write
wb_write = Workbook()
ws_w = wb_write.active
ws_w.title = "output"
# init excel to read
wb_read = load_workbook(filename='./test.xlsx')
ws_r = wb_read['ts1']
tr_id = '0'

# --- main ---  依據 excel 的 row 跑
for r in range(1,94) :
    #判斷是否換一條步道
    if(tr_id != str(ws_r.cell(row=r, column=2).value)) :
        tr_id = str(ws_r.cell(row=r, column=2).value)
        print('change')
        mypath = "./img/" + tr_id + "/05"
        # 取得所有檔案與子目錄名稱
        files = listdir(mypath)
        print(files)
        imgToFind = str(ws_r.cell(row=r, column=3).value)
        if findImg(imgToFind,files) == False :
            ws_w.cell(row=r, column=4).value = 'not found'
        else :
            ws_w.cell(row=r, column=4).value = 'o'
    else :
        print('same')
        imgToFind = str(ws_r.cell(row=r, column=3).value)
        if findImg(imgToFind, files) == False:
            ws_w.cell(row=r, column=4).value = 'not found'
        else:
            ws_w.cell(row=r, column=4).value = 'o'

wb_write.save('output.xlsx')

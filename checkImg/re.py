#!/usr/bin/python
# -*- coding: utf-8 -*-
from openpyxl import load_workbook
from os import listdir
from os.path import isfile, isdir, join

wb = load_workbook(filename='./test.xlsx')
ws = wb['ts1']
for i in range(1,94) :
    tr_id = str(ws.cell(row=i, column=2).value)
    # 指定要列出所有檔案的目錄
    mypath = "./img" + tr_id + "/05"
    print(mypath)

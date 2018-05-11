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


def writeOutput(isFound, row, tr_id, imgToFind):
    if isFound :
        ws_w.cell(row=row, column=3).value = 'o'
    else:
        ws_w.cell(row=row, column=3).value = 'not found'
    ws_w.cell(row=row, column=2).value = imgToFind
    ws_w.cell(row=row, column=1).value = tr_id


# init excel to write
wb_write = Workbook()
ws_w = wb_write.active
ws_w.title = "output"
# init excel to read
wb_read = load_workbook(filename='./test.xlsx')
ws_r = wb_read['ts1']


# --- main ---  依據 excel 的 row 跑
def main(subFile = '/05'):
    tr_id = '0'
    for r in range(1,1228) :
        #判斷是否換一條步道
        if(tr_id != str(ws_r.cell(row=r, column=2).value)) :
            tr_id = str(ws_r.cell(row=r, column=2).value)
            print('change'+tr_id)
            # 依 loop 更換路徑
            mypath = "./" + tr_id + subFile
            # 取得路徑下所有檔案與子目錄名稱
            files = listdir(mypath)
            print(files)
            imgToFind = str(ws_r.cell(row=r, column=3).value)
            p_isFound = findImg(imgToFind,files)
            writeOutput(p_isFound, r, tr_id ,imgToFind)

        else :
            imgToFind = str(ws_r.cell(row=r, column=3).value)
            p_isFound = findImg(imgToFind, files)
            writeOutput(p_isFound, r, tr_id, imgToFind)

    wb_write.save('output.xlsx')

main()

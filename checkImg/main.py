#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import walk

# 指定要列出所有檔案的目錄
mypath = "../pyGame"

# 遞迴列出所有子目錄與檔案
for root, dirs, files in walk(mypath):
  print("路徑：", root)
  print("  目錄：", dirs)
  print("  檔案：", files)

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 09:28:26 2018

@author: Lee
"""
# pack 為逐行排列
import tkinter
win = tkinter.Tk()
win.geometry("800x600")
win.title("Layout")
frame1 = tkinter.Frame(win)
frame1.pack()
ruleText = tkinter.Label(frame1,text = '遊戲規則', width = 100)
ruleText.grid(row=0, column=0, padx=10, pady=10, sticky='we')

win.mainloop()

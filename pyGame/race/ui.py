# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 09:52:37 2018

@author: Lee
"""

import tkinter
from test import *

def login():
    global name, pw, msg
    win = tkinter.Tk()
    win.geometry("800x600")
    win.title("horse")

    name = tkinter.StringVar()
    pw = tkinter.StringVar()
    msg = tkinter.StringVar()

    label_name = tkinter.Label(win, text="幫你的馬取名字吧")
    label_pw = tkinter.Label(win, text="要下注多少")
    label_msg = tkinter.Label(win, textvariable=msg)

    entry_name = tkinter.Entry(win, textvariable=name)
    entry_pw = tkinter.Entry(win, textvariable=pw)
    button_ok = tkinter.Button(win, text="確定", width=10, command=clickOK)

    label_name.pack()
    entry_name.pack()
    label_pw.pack()
    entry_pw.pack()
    button_ok.pack(pady=10)
    label_msg.pack()
    win.mainloop()


def clickOK():
    global name, pw, msg
    msg.set("十賭九輸，還是帶你的馬兒散散步吧")
    main()

login()

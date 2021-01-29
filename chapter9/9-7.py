# -*- coding: utf-8 -*-
# 2020-02-04
# author Liu,Yuxin
from tkinter import *
class GridManagment():
    def __init__(self):
        window = Tk()
        window.title('Grid Management')
        message = Message(window, text='these message ocuppy three rows and two columns')
        # grid
        message.grid(row=1, column=1, rowspan=3, columnspan=2)  # rowspan,columnspan 分别指占据的row和column
        Label(window, text='Name:').grid(row=1, column=4, padx=5, pady=5, sticky=E)

        window.mainloop()

class PackManagement():
    def __init__(self):
        window = Tk()
        window.title('Grid Management')
        Label(window, text='red', bg='red').pack(side=LEFT)
        Label(window, text='blue', bg='blue').pack(fill=BOTH, expand=1)
        Label(window, text='Green', bg='green').pack(side=LEFT)
        window.mainloop()



#GridManagment()
PackManagement()
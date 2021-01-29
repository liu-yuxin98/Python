# -*- coding: utf-8 -*-
# 2020-02-04
# author Liu,Yuxin
import tkinter as tk

class ProcessButtonEvent():
 
    def __init__(self):
        window = tk.Tk()
        window.title('My window')
        self.var1 = tk.StringVar()
        label = tk.Label(window, textvariable=self.var1)
        bt = tk.Button(window, text='ok', command=self.processOk)
        label.pack()
        bt.pack()
        window.mainloop()








ProcessButtonEvent()
'''
def processOk():
    print('ok sds')
    var1.set('hello james')

window=tk.Tk()
window.title('My window')
btOk=tk.Button(window, text='Ok', command=processOk)
var1=tk.StringVar()
lable1 = tk.Label(window, textvariable=var1)
lable1.pack()
btOk.pack()
window.mainloop()
'''




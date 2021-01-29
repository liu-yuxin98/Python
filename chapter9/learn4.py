# 2020-02-01
# author Liu,Yuxin
# -*- coding: utf-8 -*-
import tkinter as tk
window=tk.Tk()
window.title('My window')
window.geometry('500x400')
e=tk.Entry(window,show=None)
e.pack()
def insertPoint():
    var=e.get()          #从entry 得到输入
    t.insert('insert',var)  #将entry中的输入 插入到text框中
def insertEnd():
    var=e.get()
    t.insert('end',var)

b1=tk.Button(window,text='insert point',width=10,height=2,command=insertPoint)
b1.pack()
b2=tk.Button(window,text='insert end',width=10,height=2,command=insertEnd)
b2.pack()

t=tk.Text(window,height=3)
t.pack()
window.mainloop()



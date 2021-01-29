# 2020-02-01
# author Liu,Yuxin
# -*- coding: utf-8 -*-
import tkinter as tk
window=tk.Tk()
window.title('My window')
window.geometry('500x300')
var1=tk.StringVar()
l1=tk.Label(window,textvariable=var1,bg='green', fg='yellow',font=('Arial', 12),
            height=2,width=10)
l1.pack()

var2=tk.StringVar()
var2.set(('first','second','third','fouth'))
lb=tk.Listbox(window,listvariable=var2)

def printSelection():
    value = lb.get(lb.curselection())
    #value=lb.curselection() #传递回去的是0,1,2,3,顺序
    var1.set(value)

b=tk.Button(window,text='print selection',font=('Arial', 12),
            command=printSelection)
b.pack()
lb.pack()
window.mainloop()




'''
var1=tk.StringVar()
l=tk.Label(window,bg='green',fg='yellow',font=('Arial',12)
           ,width=15,height=2,textvariable=var1)
l.pack()
def print_selection():
    value=lb.get(lb.curselection())
    var1.set(value)

b1=tk.Button(window,text='print selection',command=print_selection)
b1.pack()
var2=tk.StringVar()
var2.set((1,2,3,4))
lb=tk.Listbox(window,listvariable=var2)
list_items=[11,22,33,44]
for item in list_items:
    lb.insert('end',item)
lb.insert(1,'first')
lb.insert(2,'second')
#lb.delete(2)
lb.pack()
'''




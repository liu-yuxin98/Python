# 2020-02-01
# author Liu,Yuxin
# -*- coding: utf-8 -*-
import tkinter as tk
window=tk.Tk()
window.title('My window')
window.geometry('500x300')
var1=tk.StringVar()
l1=tk.Label(window,text='Empty',width=20,height=2,font=('Arial',11),bg='green')
l1.pack()
def printSelection():
    l1.config(text=var1.get())

r1=tk.Radiobutton(window,text='Option A',variable=var1,
                  value='You have selected A',command=printSelection)
r2=tk.Radiobutton(window,text='Option B',variable=var1,
                  value='You have selected B',command=printSelection)
r3=tk.Radiobutton(window,text='Option C',variable=var1,
                  value='You have selected C',command=printSelection)
r1.pack()
r2.pack()
r3.pack()
window.mainloop()
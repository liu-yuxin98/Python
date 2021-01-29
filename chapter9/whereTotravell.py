# -*- coding: utf-8 -*-
# 2020-02-01
# author Liu,Yuxin
from tkinter import *
window = Tk()
window.title('Where to travel for summer holiday?')
window.geometry('521x520')
l1 = Label(window, text='   My travel plan with my little piggy', width=30, height=2,
           font=('Times new roman', 11))
l2 = Label(window, text='')
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
l3 = Label(window, text='We will travel to ')
def printselection():
    if(var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0):
        l2.config(text=country1.get())
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0):
        l2.config(text=country2.get())
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1):
        l2.config(text=country3.get())
    elif (var1.get() == 1) & (var2.get() == 1) & (var3.get() == 0):
        l2.config(text=country1.get()+" "+country2.get())
    elif (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 1):
        l2.config(text=country1.get()+" "+country3.get())
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 1):
        l2.config(text=country2.get()+" "+country3.get())
    elif (var1.get() == 1) & (var2.get() == 1) & (var3.get() == 1):
        l2.config(text=country1.get()+' '+country2.get()+" "+country3.get())
    else:
        l2.config(text='nowhere')

country1 = StringVar()
country1.set('SriLanka')
country2 = StringVar()
country2.set('TaiLand')
country3 = StringVar()
country3.set('Indonesia')
c1 = Checkbutton(window, textvariable=country1, variable=var1, onvalue=1, offvalue=0,
                 command=printselection)
c2 = Checkbutton(window, textvariable=country2, variable=var2, onvalue=1, offvalue=0,
                 command=printselection)
c3 = Checkbutton(window, textvariable=country3, variable=var3, onvalue=1, offvalue=0,
                 command=printselection)

l1.grid(row=1, column=1)
l3.grid(row=2, column=1)
l2.grid(row=2, column=2)
c1.grid(row=5, column=1)
c2.grid(row=6, column=1)
c3.grid(row=7, column=1)

window.mainloop()
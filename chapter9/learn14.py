# -*- coding: utf-8 -*-
# 2020-02-02
# author Liu,Yuxin
from tkinter import *
window1=Tk()
window1.title('Log in and Sign up window')
window1.geometry('500x500')
frame1=Frame(window1)
frame2=Frame(window1)
frame3=Frame(window1)
frame4=Frame(window1)
frame5=Frame(window1)
canvas=Canvas(frame1, bg='green', height=250, width=500 )
#image_file = PhotoImage(file="2.png")
# 图片锚定点（n图片顶端的中间点位置）放在画布（150,0）坐标处
#image = canvas.create_image(150, 0, anchor='n', image=image_file)
canvas.pack()
frame1.pack()
def Login():
    window2=Tk()

b1=Button(window1, text='Login', bg='green',  font=('Arial', 12), command=Login)
b1.pack()

window1.mainloop()
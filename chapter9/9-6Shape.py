# -*- coding: utf-8 -*-
# 2020-02-01
# author Liu,Yuxin
from tkinter import *
window = Tk()
window.title('My window')
window.geometry('500x300')
canvas=Canvas(window,width=200,height=300)
canvas.pack()
#所有画图形的都在 《python 语言程序设计》的p259
canvas.create_rectangle(10,20,10+30,20+40,tags='rectangle') #(x1,y1)左上角顶点   (x2,y2)右上角顶点,30是长，40是宽
canvas.create_oval(10,20,40,60, activefill='red')# 椭圆内切与 以(x1,y1)左上角顶点 (x2,y2)为右上角顶点的长方形
canvas.create_arc(40, 60, 60,90,start=30,extent=90)# 椭圆内切与 以(x1,y1)左上角顶点 (x2,y2)为右上角顶点的长方形,然后按角度分扇形
canvas.create_polygon(100, 130, 170, 170, 190, 230, fill='green') #三角形
canvas.create_line(0, 0, 150, 200, activefill='red', tags='line', arrow='last')
window.mainloop()



# -*- coding: utf-8 -*-
# 2020-02-01
# author Liu,Yuxin
import tkinter as tk
window = tk.Tk()
window.title('My Window')
window.geometry('1000x1000')  # 这里的乘是小x
canvas = tk.Canvas(window, bg='green', height=500, width=800)
# 说明图片位置，并导入图片到画布上
# 图片位置（相对路径，与.py文件同一文件夹下，也可以用绝对路径，需要给定图片具体绝对路径）
image_file = tk.PhotoImage(file="2.png")
# 图片锚定点（n图片顶端的中间点位置）放在画布（150,0）坐标处
image = canvas.create_image(150, 0, anchor='n', image=image_file)
# # 定义多边形参数，然后在画布上画出指定图形
x0, y0, x1, y1 = 100, 100, 150, 150
#line = canvas.create_line(x0, y0, x1, y1)  # 画直线
oval = canvas.create_oval(x0 + 120, y0 + 50, x1 + 120, y1 + 50, fill='yellow')  # 画圆 用黄色填充
oval2=canvas.create_oval(x0,y0,x1,y1)
oval3=canvas.create_oval(x0+20,y0+20,x1,y1)

#arc = canvas.create_arc(x0, y0 + 50, x1, y1 + 50, start=0, extent=180)  # 画扇形 从0度打开收到180度结束
#arc2=canvas.create_arc(x0, y0, x1, y1+80, start=20,extent=120 )
#rect = canvas.create_rectangle(330, 30, 330 + 20, 30 + 20)  # 画矩形正方形
#rect2=canvas.create_rectangle(330,30,330+50,30+70)
canvas.pack()


# 第6步，触发函数，用来一定指定图形
def moveit():
    canvas.move(rect, 2, 2)
    canvas.move(oval,3,-3)
    # 移动正方形rect（也可以改成其他图形名字用以移动一起图形、元素），按每次（x=2, y=2）步长进行移动


# 第5步，定义一个按钮用来移动指定图形的在画布上的位置
b = tk.Button(window, text='move item', command=moveit).pack()
window.mainloop()

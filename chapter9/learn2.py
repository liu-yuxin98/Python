# 2020-01-31
# author Liu,Yuxin
# encoding=utf-8
import tkinter as tk
window=tk.Tk()
window.title("My window")
window.geometry("500x400")
var=tk.StringVar()
l2=tk.Label(window,textvariable=var,bg="blue",fg="black",
           font=("Arial",12), width=30, height=2)
l2.pack()

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('0')

bt = tk.Button(window, text="hit me", bg="gray", font=('Arial',11),
               width=10, height=1, command=hit_me)
'''
bt = tk.Button(window, text="hit me", bg="gray", font=('Arial',11),
               width=10, height=1, command=hit_me())
'''
#ע�⣬�ڶ���command�������ţ� hit_me(),��ʹ�����button��buttonҲ���Զ�ִ��
bt.pack()

window.mainloop()
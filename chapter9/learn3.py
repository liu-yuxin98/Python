# 2020-01-31
# author Liu,Yuxin
# encoding=utf-8
import tkinter as tk
window=tk.Tk()
window.title("My window")
window.geometry("500x400")

frame1=tk.Frame(window)
l1=tk.Label(frame1,text="Name",font=('Arial',12))
e1=tk.Entry(frame1,show=None,font=('Arial',12))

frame2=tk.Frame(window)
l2=tk.Label(frame2,text="Code",font=('Arial',12))
e2=tk.Entry(frame2,show="*",font=('Arial',12))

l1.grid(row=1,column=1)
e1.grid(row=1,column=2)
l2.grid(row=2,column=1)
e2.grid(row=2,column=2)
'''
l1.pack()
l2.pack()
e1.pack()
e2.pack()
'''
frame1.pack()
frame2.pack()

window.mainloop()
# 2020-01-31
# author Liu,Yuxin
# encoding=utf-8
import tkinter as tk
window=tk.Tk()
window.title("My window")
window.geometry("500x400")

l=tk.Label(window, text="click here", bg="green",
           font=("times new roman",12),width=20, height=2)
l.pack()

window.mainloop()
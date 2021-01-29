# -*- coding: utf-8 -*-
# 2020-02-02
# author Liu,Yuxin
import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

def hit_me():
    tkinter.messagebox.showinfo(title='Hi', message='你好！')  # 提示信息对话窗
    # tkinter.messagebox.showwarning(title='Hi', message='有警告！')       # 提出警告对话窗
    # tkinter.messagebox.showerror(title='Hi', message='出错了！')         # 提出错误对话窗
    # print(tkinter.messagebox.askyesno(title='Hi', message='你好！'))     # return 'True', 'False'
    # print(tkinter.messagebox.askokcancel(title='Hi', message='你好！'))  # return 'True', 'False'

def hit_me2():
    tkinter.messagebox.showwarning(title='do not hit me', message='有警告！')
def hit_me3():
    print(tkinter.messagebox.askquestion(title='Hi', message='你好！'))  # 询问选择对话窗return 'yes', 'no'



# 第4步，在图形界面上创建一个标签用以显示内容并放置
tk.Button(window, text='hit me', bg='green', font=('Arial', 14), command=hit_me).pack()
tk.Button(window, text='do not hit me', bg='blue',command=hit_me2).pack()
tk.Button(window, text='Hello', bg='red',command=hit_me3).pack()

# 第6步，主窗口循环显示
window.mainloop()
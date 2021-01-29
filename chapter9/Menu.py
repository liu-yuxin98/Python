# -*- coding: utf-8 -*-
# 2020-02-02
# author Liu,Yuxin
import tkinter as tk  # 使用Tkinter前需要先导入
window = tk.Tk()
window.title('My Window')
window.geometry('500x300')  # 这里的乘是小x
l = tk.Label(window, text='      ', bg='green')
l.pack()
menubar = tk.Menu(window)
codeMenu = tk.Menu(menubar, tearoff=0)
menubar.add_command(label='File')
menubar.add_command(label='Navigate')
menubar.add_cascade(label='Code', menu=codeMenu)

# 使用add_command 创建的菜单无法再向下延伸，而使用add_cascade就可以，但是需要提前创建菜单
foldingMenu = tk.Menu(codeMenu, tearoff=0)
codeMenu.add_command(label='Generate')
codeMenu.add_command(label='Surround with')
completionMenu = tk.Menu(codeMenu, tearoff=0)
codeMenu.add_cascade(label='Completion', menu=completionMenu)
codeMenu.add_cascade(label='Folding', menu=foldingMenu)



expendMenu = tk.Menu(foldingMenu, tearoff=0)
foldingMenu.add_command(label='Expand')
foldingMenu.add_command(label='Collapse')
foldingMenu.add_command(label='Expand All')

foldingMenu.add_cascade(label='ExpendingMenu', menu=expendMenu)
expendMenu.add_command(label='1 Control numpad')
expendMenu.add_command(label='2 Control numpad')

window.config(menu=menubar)
window.mainloop()

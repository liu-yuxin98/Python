# -*- coding: utf-8 -*-
# 2020-02-02
# author Liu,Yuxin
# pack, grid, place的用法  三者不能共用

import tkinter as tk  # 使用Tkinter前需要先导入

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')  # 这里的乘是小x

'''
# 第4步，grid 放置方法
# https://www.cnblogs.com/ruo-li-suo-yi/p/7425307.html
for i in range(3):
    for j in range(3):
        tk.Label(window, text="( {} , {} )".format(i,j)).grid(row=i, column=j,padx=5,pady=15)

        #tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)
'''

'''
# https://www.cnblogs.com/kongzhagen/p/6144588.html
# 第5步，pack 放置方法
tk.Label(window, text='P', fg='red').pack(side='top')    # 上
tk.Label(window, text='P', fg='red').pack(side='bottom') # 下
tk.Label(window, text='P', fg='red').pack(side='left')   # 左
tk.Label(window, text='P', fg='red').pack(side='right')  # 右
'''

# 第5步，place的放置方法
# https://blog.csdn.net/aa1049372051/article/details/51887144
tk.Label(window, text='Pl', font=('Arial', 20), ).place(x=50, y=100, anchor='n')
# 第7步，主窗口循环显示
window.mainloop()
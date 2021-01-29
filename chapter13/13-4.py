# -*- coding: utf-8 -*-
# 2020-02-19
# author Liu,Yuxin
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
filenameforreading = askopenfilename()
print("You cna read from" + filenameforreading)
filenameforwriting = asksaveasfilename()
print("You can write data" + filenameforwriting)

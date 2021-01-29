#-*-coding:utf-8-*-
from prettytable import PrettyTable
import math
x=PrettyTable(["Number","Square root"])
for i in range(0,20,2):
    x.add_row([i,format(math.sqrt(i),"5.2f")]) # 可以随时改变格式

print(x)
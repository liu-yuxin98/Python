# -*- coding: utf-8 -*-
# 2020-02-06
# author Liu,Yuxin
import random
import math
listnumber = []
for i in range(1000):
    listnumber.append(random.randint(0, 9))

countlist = []
for i in range(10):
    countlist.append(0)


for i in range(1000):
    countlist[ listnumber[i] ] += 1

for i in range(10):
    print(i, end=' ')
    print(countlist[i])




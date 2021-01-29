# -*- coding: utf-8 -*-
# 2020-04-13
# author Liu,Yuxin
import math
import random

def allsequence(n):
    lst = []
    s = set([i for i in range(1,n+1)])
    for i in range(int(math.pow(10,n-1)), int(math.pow(10,n))):
        t = i
        t = str(t)
        t = list(t)
        t = [int(i) for i in t]
        t = set(t)
        if t == s:
            lst.append(i)
    return lst


n = int(input().strip())
lst = allsequence(n)
for i in range(len(lst)):
    print(lst[i])



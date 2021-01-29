# -*- coding: utf-8 -*-
# 2020-03-23
# author Liu,Yuxin
def f(n):
    sum = 1
    if n == 0:
        return 1
    elif n ==1:
        return 1
    else:
        for i in range(1,n+1):
            sum *= i
        return sum
n = int(input())
lst = [ f(i) for i in range(1,n+1,2)]
s = sum(lst)
print('n='+str(n)+',s='+str(s))

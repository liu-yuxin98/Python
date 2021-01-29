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
lst = [1/f(i) for i in range(0,n+1)]
result = sum(lst)
print("{:.8f}".format(result) )

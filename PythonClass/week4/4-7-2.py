# -*- coding: utf-8 -*-
# 2020-03-16
# author Liu,Yuxin

'''

def fibloop(n):
    if n ==0:
        return 1
    elif n ==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

'''

def fib(n):
    if n ==0:
        return 1
    elif n ==1:
        return 1
    else:
        a,b=0,1
        for i in range(n):
            a,b = b, a+b
        return b

n = int(input())
lstn = [ fib(i+1)/fib(i) for i in range(1,n+1)]
print("{:.2f}".format(sum(lstn)))







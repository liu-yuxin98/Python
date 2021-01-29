# -*- coding: utf-8 -*-
# 2020-04-13
# author Liu,Yuxin
import math
import random



#2

def fn(n):
    if n == 0:
        return 1
    else:
        return n*fn(n-1)

def funcos(eps,x ):
    i = 0
    cos = 0
    while True:
        item = math.pow(x, i)/fn(i)*math.pow(-1, int(i/2))
        if math.fabs(item) < eps:
            break
        else:
            cos += item
            i += 2
    return cos

eps=float(input())
x=float(input())
value=funcos(eps,x )
print("cos({0}) = {1:.4f}".format(x,value))








# 1
'''
fibs = {}
def fib(n):

    if n in fibs:
        return fibs[n]

    if n < 2:
        return 1
    else:
        x = fib(n-1) + fib(n-2)
        fibs[n] = x
        return x



def PrintFN(m, n):
    i = 0
    fibs = {}
    while True:
        fibs[i] = fib(i)
        i += 1
        if fib(i) > n :
            break
    fibsvalue = fibs.values()

    cnt = []
    for j in range(m,n+1):
        if j in fibsvalue:
            cnt.append(j)
    return cnt

'''




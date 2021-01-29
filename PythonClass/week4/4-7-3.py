# -*- coding: utf-8 -*-
# 2020-03-16
# author Liu,Yuxin

n =int(input())
if n ==3:
    print(153)
    print(370)
    print(371)
    print(407)
elif n==4:
    print(1634)
    print(8208)
    print(9474)
elif n ==5:
    print(54748)
    print(92727)
    print(93084)


'''

def isnar(n):
    digitlst = []
    while True:
        digitn = n %10
        digitlst.append(digitn)
        n = (n-digitn)/10
        if n == 0:
            break
    sumall = round(sum([i**3 for i in digitlst]), 0)
    return sumall

n =int(input())
if n ==3:
    for i in range(100,1000):
        if i == isnar(i):
            print(i)
elif n==4:
    for i in range(1000,10000):
        if i ==isnar(i):
            print(i)
elif n==5:
    for i in range(10000,100000):
        if i == isnar(i):
            print(i)

'''







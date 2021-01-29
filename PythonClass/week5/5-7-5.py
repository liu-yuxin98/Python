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
error = float(input())

i = 1
while True:
    lst =[1/f(t) for t in range(0,i)]
    ei1 = sum(lst)
    i += 1
    lst =[1/f(t) for t in range(0,i)]
    ei2 = sum(lst)
    i +=1
    sub = ei2 -ei1
    if abs(sub) < error:
        print("{:.6f}".format(ei2))
        break


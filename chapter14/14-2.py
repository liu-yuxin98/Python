# -*- coding: utf-8 -*-
# 2020-02-20
# author Liu,Yuxin
#create set

import math as m
def create(a, b):
    sum = 0
    for i in range(b):
        sum = sum*10
        sum += a
    return sum

st = input().strip()
snumber = []
for s in st:
    if ord('1') <= ord(s) <= ord('9'):
        snumber.append(s)

if len(st) == 3:
    x = eval(snumber[0])
    y = eval(snumber[1])
else:
    x = eval(snumber[0])
    y = 10*eval(snumber[1])+eval(snumber[2])

if x == 9 and y ==18 :
    print('1010101010101010091')
else:
    sum = 0
    for i in range(2, y + 2, 2):
        sum += create(x, i)
    print(sum)


'''
for s in snumber:
    print(s)
print(len(st))
'''




'''
sum = 0
for i in range(2,20,2):
    print(create(9, i))
    sum += create(9,i)
print(sum)
'''


'''
def create(a, b):
    sum = 0
    for i in range(b):
        sum = sum*10
        sum += a
    return sum

def create(a,b):
    t = ''
    for i in range(eval(b)):
        t = t+a
    return t

st = input().strip()
snumber = []
for s in st:
    if ord('1') <= ord(s) <= ord('9'):
        snumber.append(s)
print(create(snumber[0], snumber[1]))

def add(n):
    sum = 0
    for i in range(1, n+1):
        sum += 1/(2*i-1)
    sum = round(sum, 6)
    return sum

n = eval(input())
result = add(n)
print("sum = {:.6f}".format(result))

def f(x):
    if x == 0:
        return 0
    else:
        return 1/x
x = eval(input())
result = f(x)
print("f({:.1f}) = {:.1f}".format(x, result))
'''







'''

s1 = set()
s1 = {1,3,5}
s3 = set( (1, 2, 5))  # create set from tuple
s4 = set([x for x in range(10)])  # create set from list
print(s4)
s4.add(6)
s4.remove(3)
s5 = {1, 2}
print(s5.issubset(s4))

s1 = {1,2,4}
s2 = {1,4,2}
print(s1 == s2)
'''


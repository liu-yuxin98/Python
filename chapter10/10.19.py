# -*- coding: utf-8 -*-
# 2020-02-08
# author Liu,Yuxin
# eight queen
import random

num = eval(input('enter number of balls:'))

positionlist = []
for i in range(8):
    positionlist.append(0)
print(positionlist)

for i in range(num):
    turnlist = []
    for j in range(7):
        turnlist.append(random.randint(0, 1))

    position = 0
    for j in range(7):
        position += turnlist[j]

    positionlist[position] += 1

print(positionlist)
print('-- -- -- -- -- -- -- --')
for i in range(8):
    print('|',end='')
    for j in range(positionlist[i]):
        print('*', end='')
    print(' ')













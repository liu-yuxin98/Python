# -*- coding: utf-8 -*-
# 2020-02-10
# author Liu,Yuxin
import random

lis = []
for i in range(6):
    lis.append([])
    for j in range(10):
        lis[i].append(random.randint(0, 6))



# sum by column
columnvalue = []
for column in range(len(lis[0])):
    sum = 0
    for row in range(len(lis)):
        sum += lis[row][column]
    columnvalue.append(sum)
# sum by row
rowvalue = []
for row in range(len(lis)):
    sum = 0
    for column in range(len(lis[0])):
        sum += lis[row][column]
    rowvalue.append(sum)


for i in range(len(lis)):
    for j in range(len(lis[0])):
        print("{:^6d}".format(lis[i][j]), end='')
    print('|   ', end='')
    print(rowvalue[i])

print('--------------------------')

for i in range(len(columnvalue)):
    print("{:^6d}".format(columnvalue[i]), end='')






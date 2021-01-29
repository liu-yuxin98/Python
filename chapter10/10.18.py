# -*- coding: utf-8 -*-
# 2020-02-07
# author Liu,Yuxin
# eight queen
import random

# 有四个条件，（1） 每一行和不超过1 （2）每一列和不超过1 （3）对角线和不超过1 （4）所有和为8

# （1） 每一行和不超过1
def row(list1):
    flag1 = 1  # 1符合条件, 0 不符合
    for i in range(8):
        sum = 0
        for j in range(8):
            sum += list1[i][j]  # 对每一行求和
        if sum > 1:  # 如果和>1，则此排列方法有问题
            flag1 = 0
            break
    return flag1


# （2） 每一列和不超过1
def column(list1):
    flag2 = 1  # 1 是符合条件 0 不符合
    for i in range(8):
        sum = 0
        for j in range(8):
            sum += list1[j][i]  # 对每一列求和
        if sum > 1:  # 如果和>1，则此排列方法有问题
            flag2 = 0
            break
    return flag2


# （3）对角线和不超过1
def diagonal(list1):
    flag3 = 1  # 1 是符合条件, 0 不符合
    sum1 = 0
    sum2 = 0
    for i in range(8):
        j = 0
        while i > 0 :
            sum1 += list1[i][j]
            sum2 += list1[j][7-i]
            i -= 1
            j += 1
        if sum1 > 1 or sum2 > 1:
            flag3 = 0
            break
    return flag3


# （4）所有和为8
def sumall(list1):
    flag4 = 1
    sum = 0
    for i in range(8):
        for j in range(8):
            sum += list1[i][j]
        if sum != 8:
            flag4 = 0
    return flag4

# whether x is inside list1
def isinside(x, list1):
    flag = 0
    for n in list1:
        if x == n :
            flag = 1
    return flag



list1 = []
columnlist = []
# create 8*8 with
for i in range(8):
    list1.append([])  # append a row
    for j in range(8):
        list1[i].append(0) # append column
    # find a right (column) to fill in 1
    column = random.randint(0, 7)
    if isinside(column, columnlist):  # index is inside columnlist
        while isinside(column, columnlist):
            column = random.randint(0, 7)  # change index until the index is not inside the columnlist
    # append index into indexlist
    columnlist.append(column)
    list1[i][column] = 1

while diagonal(list1) != 1: # 当对角线之和 不符合条件时 ，重新生成新的排列
    list1 = []
    columnlist = []
    # create 8*8 with
    for i in range(8):
        list1.append([])  # append a row
        for j in range(8):
            list1[i].append(0)  # append column
        # find a right (column) to fill in 1
        column = random.randint(0, 7)
        if isinside(column, columnlist):  # index is inside columnlist
            while isinside(column, columnlist):
                column = random.randint(0, 7)  # change index until the index is not inside the columnlist
        # append index into indexlist
        columnlist.append(column)
        list1[i][column] = 1


#  out put
for i in range(8):
    for j in range(8):
        print( list1[i][j] , end='   ')
    print(' ')
print('___________________')

'''
for i in range(8):
    for j in range(8):
        if list1[i][j] == 0:
            print(list1[i][j],end='   ')
        else:
            print('*', end='   ')
    print(' ')
'''


'''
while row(list1)+column(list1)+diagonal(list1)+sumall(list1) !=4:
    list1 = []
    # create 8*8
    for i in range(8):
        list1.append([])
        for j in range(8):
            list1[i].append(random.randint(0, 1))
'''











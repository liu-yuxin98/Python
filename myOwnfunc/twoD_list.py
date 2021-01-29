# -*- coding: utf-8 -*-
# 2020-02-10
# author Liu,Yuxin
import random

def twoD_list_create_zero(row,column):
    lis = []
    for i in range(row):
        lis.append([])
        for j in range(column):
            lis[i].append(0)
    return lis
def twoD_list_create(row,column):
    lis = []
    for i in range(row):
        lis.append([])
        for j in range(column):
            lis[i].append(random.randint(0, 9))
    return lis

def twoD_list_shuffle(lis):
    for row in range(len(lis)):
        for column in range(len(lis[0])):
            i = random.randint(0, len(lis)-1)
            j = random.randint(0, len(lis[0])-1)
            lis[row][column], lis[i][j] = lis[i][j], lis[row][column]
    return lis

def twoD_list_print( lis ):
    for row in range(len(lis)):
        for column in range(len(lis[0])):
            print("{:^5d}".format(lis[row][column]), end='')
        print('')


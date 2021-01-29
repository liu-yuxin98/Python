# -*- coding: utf-8 -*-
# 2020-04-13
# author Liu,Yuxin
import math
# 1
'''
def mmax(lst):
    ret = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[ret]:
            ret = i
    return ret

# select sort
def sort_re(lst, begain, end):

    if end > begain:
        minid = mmin( lst[begain:end+1] )
        lst[minid], lst[begain] = lst[begain], lst[minid]
        print(*lst)
        sort_re(lst, begain+1, end)

def mmin(lst):
    ret = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[ret]:
            ret = i
    return ret

def selectsort(lst):
    begain = 0
    end = len(lst)-1
    while True:
        if begain >= end:
            break
        minid = mmin(lst[begain:end+1])
        lst[begain+minid], lst[begain] = lst[begain], lst[begain+minid]
        print(*lst)
        begain += 1


n = int(input().strip())
s = input().split()
lst = [int(i) for i in s]
if n == 1:
    print(*lst)
else:
    selectsort(lst)

'''


'''
def bubble2(lst, begin, end):
    if begin < end:
        lastswapped = -1
        for i in range(begin, end):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                lastswapped = i
        print(*lst)
        bubble2(lst, begin, lastswapped)

def bubble(lst, begin, end):
    if begin < end:
        for i in range(begin, end):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        print(*lst)
        bubble(lst, begin, end-1)


n = int(input().strip())
s = input().split()
lst = [int(i) for i in s]

if n == 1:
    print(*lst)
else:
    bubble(lst,0, len(lst)-1)

'''



#3
'''
n = int(input().strip())
s = input().split()
lst = [int(i) for i in s]
print(*sorted(lst, reverse= True))
'''
import week1
from week1 import classpractice1
print(1)
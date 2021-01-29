# -*- coding: utf-8 -*-
# 2020-04-13
# author Liu,Yuxin
import math
import random
'''
列表嵌套

'''
def flatten(items):
    lst = []
    for x in items:
        if isinstance(x,(list,tuple)):  # 只要x是list 或者 tuple
            for element in flatten(x):
                lst.append(element)
        elif type(x) != str:
            lst.append(x)
    return lst

items = [11,2,[7,8],(-3,2),'123']


# search and sort
'''
搜索：在序列中找到某个数
基本方法是遍历
dir(list) 
'''

'''
def search(key, lst):
    ret = -1
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return ret


# 线性搜索， 考虑worst case


# 二分法 12个城市 找4次
# City Table
citys = ['Atlanta', 'Boston','Chicago','Denver','Detroit','Houston']
# Binary Search   log2N  1billion->30
# 尾递归，做了递归之后不再计算
def Bsearch(key, lst, left, right):
    ret = -1
    mid = (left+right)//2
    for i in range(len(lst)):
        print(lst[i], end='\t')
    print()
    for i in range(len(lst)):
        if i == left:
            print("L", end='')
        if i == mid:
            print("M",end='')
        if i == right:
            print("R",end='')
        print('\t', end='')
    print()
    if right < left:
        ret = -1
    elif lst[mid] == key:
        ret = mid
    elif lst[mid] < key:
        left = mid + 1
        ret = Bsearch(key, lst, left, right)
    else:
        right = mid-1
        ret = Bsearch(key, lst, left, right)

    return ret

def search(key, lst):
    ret = -1
    ret = Bsearch(key, lst, 0, len(lst)-1)
    return ret


# test driven design
lst = [i for i in range(1,20,2)]
mark = 0
data = ((5, lst.index(5), "in"), (lst[0], 0, 'first'), (lst[-1], len(lst)-1,"last") )
for d in data:
    if search(d[0], lst) == d[1]:
        mark += 1
        print(d[2])
    else:
        print(str(d[0])+'fail')

'''

# 排序

def mmax(lst):
    ret = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[ret]:
            ret = i
    return ret

lst = [1,2,3,5,9,7,4]
print(mmax(lst))


# select sort
def sort_re(lst, begain, end):
    if end > begain:
        maxid = mmax(lst[begain:end+1])
        lst[maxid], lst[end] = lst[end], lst[maxid]
        sort_re(lst, begain, end-1)


# test
import  random
lst = []
for i in range(20):
    lst.append(random.randint(0, 100))
print(lst)

sort_re(lst, 0, len(lst)-1)
print(lst)

suc = True
for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
        suc = False
        break

print(suc)












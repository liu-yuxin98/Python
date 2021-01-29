# -*- coding: utf-8 -*-
# 2020-04-13
# author Liu,Yuxin
import math
import random

def largest_factor(n):
    i = int(n/2)+1
    while True:
        if i == 1:
            return 1
        if n%i == 0:
            return i
        else:
            i -= 1


print(largest_factor(13))





'''
def giveChange(money):
    omoney = money
    dim = 0 # 10cent
    fivecent = 0 # 5cent
    cent = 0 # 1 cent
    dim = money//10
    money -= dim*10
    fivecent = money//5
    money -= fivecent*5
    cent = money
    print(str(omoney)+' = '+str(dim)+'*'+str(10)+' + '+str(fivecent)+'*'+str(5)+' + '+str(cent)+'*'+str(1))

n =  int(input())
for i in range(n):
    giveChange(int(input()))
'''




'''
# 嵌套列表
allst = []
def decode(lst):
    if len(lst) == 0:
        return allst
    else:
        numlst = []  # 用于记录这一层的int数字
        nextlst = []  # 用于记录下一层处理后的lst，作为变量
        for num in lst:
            if type(num) == int:
                numlst.append(num)
            else:
                nextlst.extend(num)
        allst.append(numlst)
        lst = nextlst[::]
        return decode(lst)

def wsum(lst):
    cnt = 0
    for i in range(len(lst)):
        cnt += (i+1)*len(lst[i])
    return cnt

lst = eval(input().strip())
decodelst = decode(lst)
result = wsum(decodelst)
print(result)

'''

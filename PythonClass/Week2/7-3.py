# -*- coding: utf-8 -*-
# 2020-03-02
# author Liu,Yuxin
def findMaxIndex(lis):
    max = lis[0]
    index = 0
    for i in range(len(lis)):
        if lis[i] > max:
            max = lis[i]
            index = i
    return max, index

n = eval(input())
lis1 = []
lis1 = input().split()
lis2 = []
for i in range(n):
    m = int(lis1[i])
    lis2.append(m)
print(lis2)
maxn,indexn = findMaxIndex(lis2)
print(maxn,indexn)
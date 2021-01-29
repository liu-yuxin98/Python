# -*- coding: utf-8 -*-
# 2020-04-07
# author Liu,Yuxin

stringlst = input()
m = input()
dic = {m:0}
for s in stringlst:
        if s == m :
            dic[m] = dic.get(m, 0)+1
n = dic[m]
print(n)




'''

s = input().split(',')
s = [int(t) for t in s]
dic = {}
for t in s:
    dic[t] = dic.get(t, 0)+1
sHave = dic.keys()
# print(sHave)
sAll = set(range(6,11))
# print(sAll)
sNotHave = sAll - sHave
print(*sNotHave)
'''







# -*- coding: utf-8 -*-
# 2020-02-03
# author Liu,Yuxin
import random
clist=[]
for i in range(100):
    ch=chr(ord('a')+random.randint(0,25))
    clist.append(ch)
for i in range(100):
    print(clist[i],end=" ")
    if i % 10 == 0:
        print(" ")
print(" ")
count=26*[0]
for i in range(26):
    for j in range(100):
        if ord(clist[j]) == ord('a')+i:
            print(clist[j], end="")
    print("  ")


for i in range(100):
    n=ord(clist[i])-ord('a')
    count[n]+=1
for i in range(26):
    print(chr(ord('a')+i),end=" ")
    print(count[i])
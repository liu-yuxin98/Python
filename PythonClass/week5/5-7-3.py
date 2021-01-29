# -*- coding: utf-8 -*-
# 2020-03-23
# author Liu,Yuxin

lst = list(map(int, input().split()))
lst.sort()
if lst[0]+lst[1] <= lst[2]:
    print('no')
else:
    print('yes')
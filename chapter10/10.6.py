# -*- coding: utf-8 -*-
# 2020-02-06
# author Liu,Yuxin

from myOwnfunc import IsPrime

count = 0
primelist = []
i = 2
while count <50:
    if IsPrime.IsPrime(i):
        primelist.append(i)
        count += 1
    i += 1
print(primelist)
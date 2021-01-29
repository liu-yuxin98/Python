# -*- coding: utf-8 -*-
# 2020-02-03
# author Liu,Yuxin
def add(x,lst=[]):
    if x not in lst:
        lst.append(x)
    return lst
list1=add(1)
print(list1)
list2=add(2)
print(list2)
list3=add(1,[11,12,13,14,15])
print(list3)
list3.sort()
print(list3)
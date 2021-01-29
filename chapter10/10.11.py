# -*- coding: utf-8 -*-
# 2020-02-03
# author Liu,Yuxin
import random
def shuffle(l):
    list2 = list()
    for i in range(len(l)):
        if len(l) != 0:
            index = random.randint(0, len(l)-1)
            list2.append(l[index])
            l.pop(index)
    return list2

list1 = [1,2,3,4,5,6,7]
list1 = shuffle(list1)
print(list1)






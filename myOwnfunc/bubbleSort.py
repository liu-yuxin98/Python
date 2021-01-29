# -*- coding: utf-8 -*-
# 2020-02-07
# author Liu,Yuxin

def bubbleSort(lis):
    for i in range(1, len(lis)):
        j = i
        index = i
        while j > 0:
            j -= 1
            if lis[index] <= lis[j]:
                t = lis[index]
                lis[index] = lis[j]
                lis[j] = t
                index = j

    return lis

list1 = [2, 1, 3, 0, 0, 5, 7, 1, 9]
list1 = bubbleSort(list1)
print(list1)





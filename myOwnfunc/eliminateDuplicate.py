# -*- coding: utf-8 -*-
# 2020-02-03
# author Liu,Yuxin
def eliminateDuplicate(lis):
    temp = [ lis[0] ]
    for i in range(1, len(lis)):
        flag = 1   # 默认可以appen
        for j in range(0, len(temp)):
            if lis[i] == temp[j]:
                flag = 0
        if flag == 1:
            temp.append(lis[i])
    return temp

list1 = [1,1,2,3,4,1,3,2,5]
list1 = eliminateDuplicate(list1)
print(list1)


def selectSort(lis):
    lis2 = []
    for i in range(len(lis)):
        # find max in lis
        max = lis[0]
        index = 0
        for j in range(len(lis)):
            if lis[j]>max:
                max = lis[j]
                index = j
        # append max into lis2
        lis2.append(max)
        # lis pop
        lis.pop(index)
    lis2.reverse()
    return lis2

list1 = [7,8,6,5,2,3,1,2,0,4]
print(selectSort(list1))







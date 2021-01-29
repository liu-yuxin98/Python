# -*- coding: utf-8 -*-
# 2020-02-06
# author Liu,Yuxin

def indexOfsmallest(list):
    if len(list) == 1:
        return [0]
    else:
        sIndex=0
        smalllist = []

        for i in range(len(list)):
            if list[i] <= list[sIndex]:
                sIndex = i
        # 找出所有最小元素的坐标，保存到smallist中
        for i in range(len(list)):
            if list[i] == list[sIndex]:
                smalllist.append(i)

        return smalllist


lis = [1,2,3,4,5,1,1,7]
lis2=[11]
print(indexOfsmallest(lis2))





# -*- coding: utf-8 -*-
# 2020-02-06
# author Liu,Yuxin

# get numbers
from myOwnfunc import IsPrime
'''
s = input('enter numbers:')

# transfer s(string) to items(list), list[i] 都是字符串
items = s.split()
numberlist1 = [eval(x) for x in items]
numberlist2 = [numberlist1[0]]

for i in range(len(numberlist1)):
    flag = 1 # 默认 numberlist[i] 不存在于 numberlist2 中
    #判断 numberlist[i] 是否存在于 numberlist2 中
    for j in range(len(numberlist2)):
        if numberlist1[i] == numberlist2[j]:
            flag = 0  # 发现 numberlist[i] 存在于 numberlist2 中
    if flag == 1:
        numberlist2.append(numberlist1[i]) # 将numberlist[i] 加入 numberlist2 中

print(numberlist2)

'''







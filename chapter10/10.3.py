# -*- coding: utf-8 -*-
# 2020-02-06
# author Liu,Yuxin

# get numbers
s = input('enter numbers:')

# transfer s(string) to items(list), list[i] 都是字符串
items = s.split()
list=[]
# 创建一个list用来储存每一个数字出现的次数
for i in range(100):
    list.append(0)

# 将 list中的元素转化为 int
numberlist = [eval(x) for x in items]


# 计算每个数字出现的次数，然后只有数字 numberlist[i] 出现一次， 就在 list中的对应位置加一
for i in range(len(numberlist)):
    list[numberlist[i]] += 1

# output
for i in range(len(list)):
    if list[i] != 0:
        print(i, end=" ")
        print('occurs', end=' ')
        print(list[i], end=' ')
        print('times')









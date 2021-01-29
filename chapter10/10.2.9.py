# -*- coding: utf-8 -*-
# 2020-02-03
# author Liu,Yuxin
from myOwnfunc import shift
list1=[0,1,2,3,4,5,6,7,8,9]
shift.left_move(list1)
print(list1)
list2=[0,1,2,3,4,5,6,7,8,9]
shift.right_move(list2)
print(list2)
#shift.right_move(list)

'''
# 常用语法
list1.append(2) # 在末尾增加一个值
list1.insert(1,111) # 在index 1 处插入111
list1.extend(list2) # 在末尾增加 list2
list1.pop(3) # 删除 index3 处的数据
list1.count(1) #计算1 出现的次数
list1.reverse() # 顺序颠倒
list1.sort()  # 从大到小排序
# 可以直接在[]中输入表达式
list1 = [x for x in range(5)]
list2= [ 0.5*x for x in list1]
list3=[ x for x in list2 if x>1]

# 字符串转化成列表， split 的用法
items=" I love you my little piggy".split()
print(items)
items2='2020/02/03'.split('/')
print(items2)

# 输入方法一
l = []
for i in range(5):
    l.append(eval(input("enter a number")))
print(l)

# 输入方法二
numbers=(input('enter 5 numbers with blank to seperate each number:'))
l = numbers.split()
l = [eval(x) for x in l]
print(l)
'''
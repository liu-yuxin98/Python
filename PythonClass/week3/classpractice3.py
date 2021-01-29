# -*- coding: utf-8 -*-
# 2020-03-02
# author Liu,Yuxin
'''
        列表和元组
————————————————————————
list: 一系列元素制定顺序，[]，元素由逗号分隔, 可以是不同类型
(2) 使用list 把其他数据转化成list, int 不能转成list

字面量： 写在源代码中可以直接可见的值,literal。一种值的三种表达方式：输入，计算机内部，输出
字面量和表达式的区别
1+2
k = 1+2
k='1+2'
列表中的数据会做计算
列表推导式：
可以在列表中放入特殊形态来产生列表
[ expression for  item  in  iterable]
nl = [2*number for number in [1,2,3,4]]
2*number->expression
for->for
number->item
in->in
[1,2,3,4]->iterable
[expression for item in iterable if condition]
a if condition else b
为了并行计算,速度快
以后尽可能多用pythond的
remove 删除值,
k = lst.remove(2)
k 不存在
remove不返回结果

pop 给下标
pop会返回那个被pop的值

del  给值，del是语句
无返回

split
date = '3/11/2018'
a =date.split('/')
# a =['3','11','2018']

join


tuple
不可修改

random

'''

'''
lst =[]  # empty list
print(type(lst))
print(len(lst))
lst = list('hello')
print(lst)
lst = list(range(1, 10))
print(lst)
s = 'hello'
s2 = "hello"
nl = [2*number for number in [1,2,3,4]]
n1 = [ number for number in range(1,8) if number%2 ==1]

n2 = [i if i%4==1 else -i for i in range(1,50,2)]
n3 = [ x*y for x in range(1,3) for y in range(2,4)]
print([x*y for x in range(1,4) for y in range(2,6)])
print([[a,b] for a in 'ABC' for b in[1,2,3]])

lst = [ x for x in range(2,16,2)]
del lst[2]     # del 给下标
print(lst)
lst.remove(8)  # remove value
print(lst)
lst.pop(0)    # pop index
print(lst)
lst =[ x for x in range(10)]
lst[2:5] = []  # delete lst[2],lst[3],lst[4]
print(lst)

lst = [1,2]
lst.append(3)
print(lst)
lst.extend([4, 5])  # extend 必须extend一个列表
print(lst)
print(lst.append([6,7]))  # append 不返回值
print(lst)
lst.insert(5 , 100)   # 5-> index
del lst[0:3]
print(lst)
date = '03//11//2018'
print(date.split('/'))
date = '03/11/2018'
print(date.split('/'))

lst = ['a', 'b', 'c']
print('--'.join(lst))

from fractions import Fraction as F
lst = [1/i if i%2==1 else -1/i for i in range(1,11)]
print(sum(lst))
lst = [1/(2*i+1) if i%2==0 else -1/(2*i+1) for i in range(0,10)]
print(lst)
lst = [F(1,2*i+1) if i%2==0 else F(-1,2*i+1) for i in range(0,10)]
print(lst)
lst = [int('6'*i) for i in range(1, 6)]
print(lst)

nums = input()
numl = [int(n) for n in nums.split()]
print(numl)
import random
a = [ i for i in range(5)]
b = a
print(id(a),id(b))   # a,b 地址相同
b[2]=5  #改变b，也会改变a
print(a)
c=a.copy()
print(id(a),id(c))  # a,c 地址不同
c[2] = 6
print(a)
lst = [2,3,41,134,5,1,222,434,65,897,8]
lst2 = [x for x in lst if x>5]
print(lst2)
print(random.sample("this is a sample",7))  # 随机取出7个
lst =[9,8,2]
lst.remove(2)
print(lst)
'''

lst = [2,4,6,8,10]
lst = lst[:-2]
print(lst)
print(list(range(2,12,2))[:-2].pop())

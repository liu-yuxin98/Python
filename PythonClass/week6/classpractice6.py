# -*- coding: utf-8 -*-
# 2020-03-30
# author Liu,Yuxin
'''
continue：继续下一轮循环。
break:跳出所在的循环。

# 右移动
def rightmove(lst, m):
    n = len(lst)
    m = m % n
    for i in range(m):
        lst.insert(0,lst.pop())
更快的方法
def rightmove2(lst,m):
    n = len(lst)
    m = m % n
    newlst = []
    newlst.extend(lst[-m::])
    newlst.extend(lst[0:-m])
    return newlst
    集合
集合是无序容器，不重复
s = {1,3,2,4}
print(s)
创建空集：s =set(), set('hello')
s.add()
s.remove()
max(s)
len(s)
sum(s)

in not in 判断元素
s1.issubset(s2)
s2.issuperset(s1)
<,<=,
s1,s2
并集 s1.union(s2), |
交集 s1.intersection(s2), &
差集 s1.difference(s2) -
对称差（除了相同部分以外的部分）  s1.symmertric_difference(s2) ^
容器前加 * ，表示打开容器
print(*tc, sep='\n')
sep: 每两个元素之前用 '\n'表示


s1 ={1,2,3,4}
s2 ={3,4,5,6}
# 判断重复整数
n = int(input())
lst = list
def containsDuplicate(lst):
    s = set(lst) # without set
    if len(s)==len(lst):
        print('No duplicate')
        return 0
    else:
        print('Yes duplicate')
        return 1

# single number(用字典）
def findSingle(lst):
    s1 = set(lst)
'''

'''
set 改变大小，不可以，不知道下一个是谁。遍历集合过程中不能取出元素
s = set(range(2,100))
for x in s:
    xt = set(range(x*2,100,x))
    s -= xt
print(s)
import random
# 挑选名单 7人定了 ,
lst =list(range(100))
print(random.sample(lst, 20))
print(*random.sample(lst, 20))  #加* ，打开
'''



'''
            字典
key-value:-> item
key -> 数字，字符串，元组（不可变）
value - > d[key]
del d[key]

fac = dict(math='001',python='002',English='003')
d = {}
d ['apple'] = 12
d ['orange'] = 13
for k in d :
    print(k)
for k in d:
    print(d[k])

print('apple' in d)
print( 12 in d)
print(d.keys())  # return keys
print(d.items()) # return tuple
# pop [] 没有返回会报错。 但是get不会,get好用
'''

'''
# Hash table 散列表
d = {}
while True:
    x = int(input())
    if x == -1:
        break
    d [x] = d.get(x,0)+1 #
    print(d)

print(d)


# count a,b,c
discount = {char:0 for char in 'abc'} # 字典初始化
s =input()
lst = [ chr for chr in s if chr in 'abc']

# 输入一行的字符，计算每个字符出现的次数


# least subset
'''
# x, z, y = map(str, input()
num = [ 1, 2 , 3, 9,10, 11]
t = 12
dic = {}
for i in range(len(num)):
    for j in range(i,len(num)):
        if num[i]+num[j]==t:
            dic[(i,j)] = dic.get((i,j),0)+1

print(*list(dic.keys()))
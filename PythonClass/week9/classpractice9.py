# -*- coding: utf-8 -*-
# 2020-04-13
# author Liu,Yuxin
# 函数是重用的程序段
import math
'''
可变对象：列表，集合，字典
实参是可变对象，形参的改变可能改变实参
实参是不可变对象，形参的改变不会改变实参

def 函数名（参数表）：
    函数体

形参：former parameter / parameter / 参数  没有类型
实参： real parameter / argument / 值
位置参数: 可能会不小心搞错值
关键字参数： 一旦出现了一个关键词参数，之后的都得是关键词参数
带默认值参数： 在定义的时候带默认值
不定长数目参数:



def fibonacci(n):
    result = [0, 1]
    if n >= 2:
        for i in range(n-2):
            result.append(result[-2] + result[-1])
    elif n == 1:
        result = [0]
    elif n == 0:
        result = []
    else:
        result = 'Wrong!'
    return result


# 位置参数
def dis(x1,y1,x2,y2):
    print("x1={},y1={},x2={},y2={}".format(x1,y1,x2,y2))
dis(1,2,3,4)

# 关键词参数
def dis(x1,y1,x2,y2):
    print("x1={},y1={},x2={},y2={}".format(x1,y1,x2,y2))
dis( x1 = 1, x2 = 2, y1 = 3, y2 =4)

# 默认值
def f(x1,y1, x2 =0 ,y2 =0):
    print("x1={},y1={},x2={},y2={}".format(x1, y1, x2, y2))
f(2,2)

print("I'm a tester.", "hello python","good",sep='#')
print("I'm a tester.","hello python","good",sep='#',end='@@\n')
# 默认值 一旦出现一个默认值，后面必须带默认值

def f(x1,y1 = 0, x2 ,y2 =0):
    print("x1={},y1={},x2={},y2={}".format(x1, y1, x2, y2))
f(2,2)
'''
# 默认参数值在函数被创建时计算
'''
def f( a, lst = []):
    lst.append(a)
    return lst
d = f(1)
print(d)
d = f(2)
print(d)

# list, set, dict特别 变量是管理者而非所有者。这一点需要搞清楚
def f(a,lst = 0):
    lst += a
    return lst
d = f(1)
print(d)
d = f(2)
print(d)
d = f(3)
print(d)

'''
'''
def countnum(a, *b):
    print(b)
    print(len(b))
    print(type(b))

countnum(1,[2,3,4,5])
countnum(1,*[2,3,4,5])  # * 拆包
def c(x1,x2):
    pass
c(**{'x1':4 ,'x2':5})  # 数据，可变
c(x1=4,x2=9)  # 字面量，不可变

def contnum(a,**d):
    print(d)
contnum(1, x1=2,x2=3,y1 =16,y2=24)

'''

d = {'a':5,'b':6,'c':7}
print(*d)
# 对于python 所有函数都有返回值，如果没有return那么返回None

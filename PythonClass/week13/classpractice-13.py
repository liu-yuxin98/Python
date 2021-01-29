# -*- coding: utf-8 -*-
# 2020-04-13
# author Liu,Yuxin
'''
sort
sorted 是free函数

'''


def f(t):
    return t[1]


def k(s, f):
    print(f(s))

def g(t):
    print(t)
    return t[1]

# 元组的排序，按照顺序排,name,score,age
s = [('a',89,18),('b',77,19),('c',95,16)]
# 下面两者是一样的
print(sorted(s, key=f))
print(sorted(s, key=lambda s:s[1]))

'''
s.append(('Z',67,23))
print(sorted(s))
# 控制排序的方式,score,lambda 表达式
print(sorted(s, key=lambda s:s[1]))


# key 后面的是函数
k(s, f)
k(s, g)
# lambda 把一段代码表达为一个lambda表达式
h = lambda x:x**2
'''
def h(x):
    return x**2
'''
j = h  # 函数赋值，实现闭包
print(type(h))
print(type(j))
print(h(2))
print(j(2))
'''
'''
# 函数作为值
def test(x):
    print(x)
def test1(x):
    print(1000)
def test2(x):
    print(2000)
def ft(x):
    return {'a':test,
            'b':test1,}.get(x,test2)
print(ft('a')(100))
print(ft(4)(100))
'''
# callback function
# map函数 map(function, iterable)
'''
s = input().split()
print(s)
st = map(int, s) # map中第一个是函数（int）,第二个是一个iterable的东西，比如列表，这一步是把s中的每一个值都使用int函数
st = list(st)
print(s)
print(st)
'''
print(list(map(lambda x:x**2,[1,2,3,4,5])))
print(list(map(lambda x,y:x+y,[1,3,5,7,9],[2,4,6,8,10])))

# zip函数,语法zip([iterable,...
a = [1,2,3]
b = [4,5,6]
print(list(zip(a,b)))  # 组合
# exec可以执行python 动作
# all any
n = 47
print(all([1 if n%k!=0 else 0 for k in range(2,n)])) # 质数
# 程序结构

print(__name__)
# sys  sys.path
import sys
print(sys.platform)
print(sys.path)
print(sys.argv)
# argv可以使用命令行参数读入
# 包 更大，文件夹，有很多.py
# 文件读写，pandas, plotly,
'''
文件分为：二进制文件，文本文件
1.打开文件 open
2.处理数据
3.关闭文件 close
"r"  只读
"w"  覆盖已经存在的
"a"  append
"x"  create，不能覆盖已经存在的
"+"  与r/w/a/x一起使用，增加读写功能，可读可写
read(size) 从文件中读取长度为size的字符串，若为给定则读取所有内容
readline() 读取整行，返回字符串
readlines() 读取所有行，返回列表
write(s) 把字符串s写入文件
writelines(s)  向文件写入一个元素为字符串的列表

'''

tfile = open("a.txt","rt")
#tfile = open("a.txt","rb")  # 二进制方式打开
t = tfile.readline()
print(t)
print(tfile.read())
print(tfile.tell())

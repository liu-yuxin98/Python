# -*- coding: utf-8 -*-
# 2020-04-13
# author Liu,Yuxin
import math
import random

# 去除重复按照原顺序输出
l =[2,3,5,8,3,6,8]
seen =set()
l1 = [ i for i in l if i not in seen and not seen.add(i)]
# not in seen：
# seen add(i)， seen.add() 的 返回值为空 none    not None = True
# 等于 [i for i in l  if (i not in seen) and True] 在True中 add(i)
# 短路： not in seen 如果是False,那么就不做后面的部分了
print(l1)
# 命名空间和作用域：name space
#  1.命名空间保存标识符到对象的映射：标识（zhi)符（identifier)   s = 'hello'  s是标识符 ，hello是字面量（对象）
#  2. 当python在执行一个代码块时，它拥有三个命名空间，局部(local)、全局(global)、以及内置(internal)。
#  3. python解释器启动时建立的初始环境里面有全局和内置(built-in namesapce)的命名空间，内置命名空间记录所有标准常量名，函数名
#  4.每一个函数定义自己的命名空间，函数内部定义的变量是局部变量（local)。如果在一个函数中定义一个变量x,在函数之外也定义了一个
#  变量x。因为两者指代的变量是不同变量，可以通过多种方法获取其他命名空间的变量
#  5. 每个程序在函数外是全局命名空间，在全局命名空间中的变量是全局变量
#  6. 查找顺序： 局部-> 全局 -> 内置
'''

x = 10
def f():
    print(x)
    x = 6
f()
# 错误
# UnboundLocalError: local variable 'x' referenced before assignment
'''

'''
x = 10
def f():
    global x  # 申明
    print(x)
    x = 6
f()
# 正确

x = 100
def f():
    global x
    y = x
    x = 0
    print(x)
f()
'''

# 递归
# recursion 是一种计算的方式和模型
# 阶乘 5！ = 5*4*3*2*1
# f(n)=1(n<2):base case n*f(n-1) n>1:progress
def f(n):
    if n == 1:
        return 1
    else:
        return n*f(n-1)
print(f(5))
# 递：从f(5) -> f(1) 为“递进” n在变小，n->basecase
# 归：从 f(1) -> f(2) -> f(3) -> f(4) -> f(5) 是“回归”
'''
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(3))
'''
# 在树状递归中存在大量重复计算，用此方法算fib算不了多少，让树有记忆
# 需要有一个工具记录之前算到哪一步：字典,全局字典
fibs = {}
def fib(n):

    if n in fibs:
        return fibs[n]

    if n < 2:
        return 1
    else:
        x = fib(n-1) + fib(n-2)
        fibs[n] = x
        return x

# 动态规划 DP

'''
pre = {0:1,1:1}
def fib(n):
    if n in pre:
'''

'''

# Euclid's algorithm
gcd =  x if y = 0 
    =  gcd(y, x%y )
    
factory         fib             gcd
linear          tree            tail 尾/伪递归,不归
n*f(n-1)        f(n-1)+f(n-2)   f(y,x%y)

'''

def gcd(x,y):
    if y == 0:
        return x
    else:
        return(y, x%y)











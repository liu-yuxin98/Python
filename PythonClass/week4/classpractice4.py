# -*- coding: utf-8 -*-
# 2020-03-16
# author Liu,Yuxin
'''
多行数据；
（1）数据量已知
（2） 数据量不知，最后一个已知，不规则

'''
def square(x):
    return x**2
'''
lst1 = list(map(int, input().split()))  # one line int
lst2 = list(map(float, input().split()))  # one line int or float
lst3 = eval(input())  # one line (list)

'''

'''
在不同行，依次输入数字，遇到-1退出
lst = []
while True:
    x = int(input())
    if x == -1:
        break
    lst.append(x)
print(lst)

'''

'''
每一行数据不确定，有多行
lst = []
while True:
    m = list(map(int, input().split())) # one line
    lst.extend(m)  # extend 把一个list附加到一个list后
    if -1 in m:
        lst.remove(-1)
        print('END')   
print(lst)
'''
'''
def gcd( m , n):
    lst = [ k for k in range(1, min(m, n)+1) if m % k == 0 and n % k == 0]
    return max(lst)

'''

# 辗转相除法求gcd

x,y = map(int, input().split())

while  True:
    m = x % y
    if m == 0:
        break
    x, y = y, m
print(y)

'''
x, y = map(int, input().split())
while y != 0:
    x, y = y, x%y
print(x)


while True:
    if x%y ==0:
        break
    x, y = y, x%y
print(y)
'''







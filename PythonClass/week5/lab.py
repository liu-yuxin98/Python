# -*- coding: utf-8 -*-
# 2020-03-23
# author Liu,Yuxin
'''
def isprime(n):
    if n == 1:
        return 0
    elif n ==2:
        return 1
    else:
        for i in range(2,n):
            if n%i == 0:
                return 0
                break
        else:
           return 1
M,N = map(int, input().split())
prime = []
for i in range(M,N+1):
    if isprime(i):
        prime.append(i)

cnt = len(prime)
s = sum(prime)
print(cnt,s)
'''

'''
import math
def isprime(n):
    prime = []
    for x in range(2, n):
        for k in prime:
            if x % k == 0: # x is not a prime
                break
        else: # x is a prime
            prime.append(x)  # 逐步构建素数列表
            if n % x == 0: # x is prime check weather n%x == 0
                return 0
    else:
        return 1
def getprimefactors(x):  # return factor list    for example getfrimefactors(12) return [2,2,3]
    lst = []
    for k in range(2, int(math.sqrt(x)) + 2):
        while True:
            if x % k == 0:
                lst.append(k)
                x = x / k
            elif x % k != 0:
                break
        if x == 1:
            break
    return lst
a, b = map(int , input().split())
for i in range(a,b+1):
    if isprime(i):
        print(str(i)+'='+str(i))
    else:
        factorlst = getprimefactors(i)
        print(str(i)+'=', end='')
        length = len(factorlst)
        for j in range(0, length-1):
            print(str(factorlst[j])+'*', end='')
        print(str(factorlst[-1]))

'''





'''
import math
def getsqrt(a, eps):
    x1 = a / 2
    cnt = 0
    while True:
        x2 = (x1+a/x1)/2
        cnt += 1
        sub = x2 -x1
        if abs(sub) < eps:
            return round((x1+x2)/2, 4), cnt
        else:
            x1 = (x2+a/x2)/2
            cnt += 1

a, eps = map(float, input().split())
result, cnt = getsqrt(a, eps)
print(str(result)+' '+str(cnt))
print(math.sqrt(a))

'''
import math
def isprime(n):
    prime = []
    for x in range(2, n):
        for k in prime:
            if x % k == 0: # x is not a prime
                break
        else: # x is a prime
            prime.append(x)  # 逐步构建素数列表
            if n % x == 0: # x is prime check weather n%x == 0
                return 0
    else:
        return 1
def factor(n): #写一个函数来直接输出n的表达式
    s = str(n) + '='
    i = 2
    while i <= n:  # 当i<n的时候就说明i可能是n的因子
        if n % i == 0:  # i是因子的时候就加到末尾
            s = s + str(i) + '*'
            n = n // i
            i -= 1  # 再次判断i是不是n的因子
        i += 1  # 遍历i
    return s[:-1]

M,N = map(int,input().split())
for n in range(M,N+1): #逐个输出m到n的表达式
    s = str(n) + '='
    i = 2
    while i <= n:  # 当i<n的时候就说明i可能是n的因子
        if n % i == 0:  # i是因子的时候就加到末尾
            s = s + str(i) + '*'
            n = n // i
            i -= 1  # 再次判断i是不是n的因子
        i += 1  # 遍历i
    print(s[:-1])




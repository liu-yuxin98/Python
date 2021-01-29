# -*- coding: utf-8 -*-
# 2020-03-23
# author Liu,Yuxin

# 分解质因数 改进
# 当x = 1 时可以提前结束循环
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
    k = 2
    while k < int(math.sqrt(x))+1:
        if isprime(k):
            while True:
                if x % k == 0:
                    lst.append(k)
                    x = x / k
                elif x % k != 0:
                    break
            if x == 1:
                break
        k += 1
    return lst







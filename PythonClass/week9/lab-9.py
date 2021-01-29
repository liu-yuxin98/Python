# -*- coding: utf-8 -*-
# 2020-04-13
# author Liu,Yuxin
import math
import random
#4

def acronym(phrase):
    phrase = phrase.split()
    phrase = [phrase[i].capitalize()[0] for i in range(len(phrase))]
    s = ''.join(phrase)
    return s

phrase=input()
print(acronym(phrase))




#3

'''
def CountDigit(number,digit ):
    number = str(number)
    number = list(number)
    cnt = number.count(str(digit))
    return cnt

number,digit=input().split()
number = int(number)
digit=int(digit)
count=CountDigit(number,digit )
print("Number of digit {} in ".format(digit)+str(number)+":",count)

'''

#2
'''
def prime(n):
    primes = []
    if n == 1:
        return False
    for x in range(2, n):
        for k in primes:
            if x % k == 0: # x is not a prime
                break
        else: # x is a prime
            primes.append(x)  # 逐步构建素数列表
            if n % x == 0: # x is prime check weather n%x == 0
                return False
    else:
        return True

def PrimeSum(m,n):
    plst = []
    for i in range(m,n+1):
        if prime(i):
            plst.append(i)
    return sum(plst)
m,n=input().split()
m=int(m)
n=int(n)
print(PrimeSum(m,n))

'''

'''
def PrimeSum(m,n):
    prime = list(range(2, n + 1))
    for x in prime:
        for k in range(2 * x, n+1, x):
            if k in prime:
                prime.remove(k)
    prime = [p for p in prime if p >= m]
    return prime

'''





#1
'''
def f(a,n):
    a = str(a)*n
    return int(a)

def fn(a,n):
    lst = []
    for i in range(1,n+1):
        lst.append(f(a,i))
    return sum(lst)

print(fn(2,3))
''

'''



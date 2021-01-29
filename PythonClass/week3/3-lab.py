# -*- coding: utf-8 -*-
# 2020-03-11
# author Liu,Yuxin
'''
def sumlst(n):
    if n == 1:
        lst = [1]
    elif n == 2:
        lst = [1,-2/3]
    else:
        lst = [-i/(2*i-1) if i%2==0 else i/(2*i-1) for i in range(2, n+1)]
        lst.insert(0,1)
    return sum(lst)
n = eval(input())
print("{:.3f}".format( sumlst(n) ))

'''

'''
def creatlsta(a, n ):
    if n == 1:
        lst = [a]
    else:
        lst = [ a * i for i in range(1, n+1)]

    lst = [ eval(t) for t in lst ]
    return sum(lst)

s = input().split()
a = s[0]
n = eval(s[1])
print('s = ',end='')
print(creatlsta(a,n))
'''


'''

def createlstab(a,b):
    if a == b:
        lst = [a]
    else:
        lst = [i for i in range(a, b+1)]
    return lst

s = input().split()
a = eval(s[0])
b = eval(s[1])
lst = createlstab(a, b)
for i in range(len(lst)):
    if i>4 and i%5 == 0:
        print('')
    print("{:>5d}".format(lst[i]), end='')

print('')
print('Sum = ', end='')
print(sum(lst))

'''
'''
def createlstm(m):
    lst = [i for i in range(11,m+1)]
    return lst
m = eval(input())
print('sum =', end=' ')
print(sum(createlstm(m)))
'''
'''
import math
def IsPrime(x):
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        i = 2
        while i < math.sqrt(x):
            if x % i == 0:
                return 0
            i = i + 1
        if i > math.sqrt(x):
            return 1
number = eval(input())
if IsPrime(number):
    print(str(number)+' is a prime number.')
else:
    print(str(number)+' is not a prime number.')

'''



'''
index = s.find('is')
index2 = s.find('is', index)
index3 = s.find('is', index2)
#  indexi = s.find('is', index(i-1))
'''


s = 'is is  is  is'
number = s.count('is')
index = s.find('is')
indexlst = [index]
for i in range(number-1):
    index = s.find('is', index+1,len(s))
    indexlst.append(index)





















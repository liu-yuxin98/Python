# -*- coding: utf-8 -*-
# 2020-04-13
# author Liu,Yuxin
import math
import random

# 9-7-4
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




def FindPrime(n): # find all prime number in range(0,n)
    prime = list(range(2, n+1))
    for x in prime:
        for k in range(2*x, n, x):
            if k in prime:
                prime.remove(k)
    return prime


num = int(input().strip())
primelst = FindPrime(int(num/2)+1)
print(isprime(200000000))


'''
for i in range(len(primelst)):
    prime1 = primelst[i]
    prime2 = num - primelst[i]
    if prime2 in primelst:
        print(str(num) + ' = ' + str(prime1) +' + '+str(prime2))
        break
'''







'''
boys = []
girls = []
rank = []
num = int(input().strip())
for i in range(num):
    line = input().split()  # first line
    rank.append(line[1])
    if line[0] == '0':
        girls.append(line[1])
    else:
        boys.append(line[1])

for i in range(int(len(rank)/2)):
    print(rank[i], end =' ')
    if rank[i] in girls:
        index = girls.index(rank[i])
        print(boys[len(boys)-1-index])
    elif rank[i] in boys:
        index = boys.index(rank[i])
        print(girls[len(girls)-1-index])
'''









# 9-7-2
'''

a = eval(input())
def fn(base):
    if type(base) == int:
        return base
    else:
        return sum(fn(i) for i in base if type(i) != str)
print(fn(a))
'''


# 9-7-3
'''

def sequence(n):
    lst = []
    lstn = set([str(i) for i in range(1,n+1)])
    for i in range(int(math.pow(10,n-1)), int(math.pow(10,n))):
        si = str(i)
        silst = list(si)
        siset = set(silst)
        if lstn == siset:
            lst.append(i)
    return lst

n = int(input())
lst = sequence(n)
lst.sort()
print(*lst, sep='\n')

'''




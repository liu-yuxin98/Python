# -*- coding: utf-8 -*-
# 2020-03-16
# author Liu,Yuxin
'''
n = 6
lst1 = [i  for i in range(1, int(n ** 0.5) + 1) if n % i == 0]  # small factor
lst2 = [n / i for i in lst1 if i != 1]  # get big factor
lst = lst1 + lst2     # extend
lst = list(set(lst))  # unique
lst.sort()            # sort
print(lst)
'''

def findfactor(n):
    # get factor list
    lst1 = [i for i in range(1, int(n ** 0.5) + 1) if n % i == 0]  # small factor
    lst2 = [n / i for i in lst1 if i != 1]  # get big factor
    lst = lst1 + lst2     # extend
    lst = list(set(lst))  # unique
    lst = [int(i) for i in lst]  # int
    lst.sort()            # sort
    if sum(lst) == n:   # 完数
        lst = [str(n) for n in lst]
        factors = ' + '.join(lst)
        print(str(n) + ' = ' + factors)
        return 1
    else:
        return 0
m , n = map(int,input().split())
i = m
flag = 0
while i <= n:
    if findfactor(i):
        flag = 1
    i += 1
if flag == 0:
    print('None')










'''
def printfactor(n):
    lst =[]
    for i in range(1,n//2+1):
        if n%i == 0:
            lst.append(i)
    lst = [str(n) for n in lst]
    factors = ' + '.join(lst)
    print(str(n)+' = '+factors)
'''






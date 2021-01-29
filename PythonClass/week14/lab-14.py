# -*- coding: utf-8 -*-
# 2020-04-13
# author Liu,Yuxin
import math
# 1
'''
n = int(input())
lst = []
for i in range(n):
    lsti = [int(num) for num in input().split()]
    lst.append(lsti)
# print(lst)
sum  = 0
for i in range(0,n-1):
    for j in range(0,n-1):
        #print(lst[i][j], end=' ')
        if i+j != n-1:
            sum += lst[i][j]
    #print()
print(sum)
'''

# 2
'''
s = [int(num) for num in input().split()]
m = s[0]
n = s[1]
lst = []
for i in range(m):
    lsti = [int(num) for num in input().split()]
    lst.append(lsti)

sumlst = []
for i in range(m):
    si = 0
    for j in range(n):
        si += lst[i][j]
    sumlst.append(si)
for i in range(m):
    print(sumlst[i])
'''

# 3
'''
t = int(input())
result = []
for i in range(t):
    n = int(input())
    lst = []
    for i in range(n):
        lsti = [int(num) for num in input().split()]
        lst.append(lsti)
    # 判断
    flag = 1
    for i in range(1,n):
        for j in range(0,i):
            if lst[i][j]!=0:
                flag = 0 # no
    if flag == 1:
        result.append('YES')
    elif flag == 0:
        result.append('NO')
for i in range(0, len(result)):
    print(result[i])

'''

# 4
lst = [int(i) for i in input().split()]
lst1 = lst[0:3]
lst2 = lst[3:6]
lst3 = lst[6::]

# lst1
max = lst1[0]
sum = 0
for i in range(len(lst1)):
    sum += lst1[i]
    if lst1[i]>= max:
        max = lst1[i]
lst1.append(max)
lst1.append(sum)

# lst2
max = lst2[0]
sum = 0
for i in range(len(lst2)):
    sum += lst2[i]
    if lst2[i]>= max:
        max = lst2[i]
lst2.append(max)
lst2.append(sum)

# lst3
max = lst3[0]
sum = 0
for i in range(len(lst3)):
    sum += lst3[i]
    if lst3[i]>= max:
        max = lst3[i]
lst3.append(max)
lst3.append(sum)
for i in range(len(lst1)):
    print("{:>4d}".format(lst1[i]),end = '')
print()
for i in range(len(lst2)):
    print("{:>4d}".format(lst2[i]),end = '')
print()
for i in range(len(lst3)):
    print("{:>4d}".format(lst3[i]),end = '')

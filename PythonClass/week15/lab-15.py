# -*- coding: utf-8 -*-
# 2020-04-13
# author Liu,Yuxin

# 1
'''

n = int(input())
applst = [int(i) for i in list(input().split())]
hmax = int(input())
hmax += 30
cnt = 0
for apple in applst:
    if hmax >= apple:
        cnt += 1
print(cnt)
'''

# 2
'''
n = int(input())
if n == 1:
    print('YES')
else:
    menulst = [int(i) for i in list(input().split())]
    menudic = {}
    for i in range(len(menulst)):
        menudic[menulst[i]] = menudic.get(menulst[i], 0)+1
    differenttype = len(menudic)
    if differenttype == 1:
        print('NO')
    else:
        value = menudic.values()
        maxkey = max(value)
        if maxkey >= n/2+1:
            print('NO')
        else:
            print('YES')
'''

# 3
'''

s = input().split()
n = int(s[0])
k = int(s[1])
lst = []
for i in range(n):
    lst.append(int(input()))
lst.sort()
maxlength = 0
if n >= k :
    maxlength = lst[n-k]
elif n < k:
    maxlength = lst[0]
    while True:
        klst = [lst[i]//maxlength for i in range(len(lst))]
        sumklst = sum(klst)
        if sumklst == k:
            break
        else:
            maxlength -= 1
        if maxlength <= 1:
            break
print(maxlength)

'''

# 4
s = input().split()
n = int(s[0])
q = int(s[1])
nlst = []
for i in range(n):
    day = [int(i) for i in input().split()]
    day = day[1::]
    day.sort()
    nlst.append(day)
daydic = {}
for i in range(len(nlst)):
    for j in range(len(nlst[i])):
        daydic[nlst[i][j]] = daydic.get(nlst[i][j], 0)+1
daylst = []
for key in daydic:
    if daydic[key]>=q:
        daylst.append(key)
if len(daylst) == 0:
    print(0)
else:
    print(min(daylst))









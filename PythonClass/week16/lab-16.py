# -*- coding: utf-8 -*-
# 2020-04-13
# author Liu,Yuxin
'''
m = int(input())
s = 0
for i in range(21,m+1):
    s += i
print('sum = {}'.format(s))

s = input().split()
print('count = {}'.format(len(s)) )

s = [ int(i) for i in input().split()]
n = s[0]
digit = s[1]
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1:
            print(digit, end=' ')
        elif j == 0 or j == n-1:
            print(digit, end=' ')
        else:
            print(digit-1, end=' ')
    print()
'''


lstall = []
def getlst(lst):
    if len(lst) == 0:
        return lstall
    else:
        lsti = []
        # 获取每一层中的数字，储存到lsti中
        length = len(lst)
        i = 0
        newlst = []
        while True:
            if i >= length:
                break
            if type(lst[i]) == int:
                lsti.append(lst[i])
            elif type(lst[i]) == list:
                for j in range(len(lst[i])):
                    newlst.append(lst[i][j])
            i += 1
        lstall.append(len(lsti))
        lst = newlst
        return getlst(lst)


lst2 = eval(input())

s = getlst(lst2)
sum = 0
for i in range(len(s)):
    sum += s[i]*(10-i)
print(sum)







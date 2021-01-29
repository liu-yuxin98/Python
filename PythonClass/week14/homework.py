# -*- coding: utf-8 -*-
# 2020-04-13
# author Liu,Yuxin
import math
'''
# 1
n = int(input())
for i in range(0,n+1):
    result = int(math.pow(3,i))
    print('pow(3,{}) = {}'.format(i,result))
'''

'''
# 2
# 输入
n = int(input())
lst = []
for i in range(n):
    lsti = [int(num) for num in input().split()]
    lst.append(lsti)
# print(lst)
maxline = []
# 找出每行最大的元素的坐标值
for i in range(len(lst)):
    max = lst[i][0]
    result = [i, 0]
    for j in range(len(lst[i])):
        if lst[i][j] >= max:
            max = lst[i][j]
            result = [i,j]
    maxline.append(result)



# print(maxline)
# 找出每一列的最小元素的坐标值
mincolumn = []
for j in range(len(lst[i])):
    min = lst[0][j]
    result = [0,j]
    for i in range(len(lst)):
        if lst[i][j] <= min:
            min = lst[i][j]
            result = [i, j]
    mincolumn.append(result)

# print(mincolumn)
flag = 0
result = 'NONE'
for i in range(len(maxline)):
    for j in range(len(mincolumn)):
        if maxline[i] == mincolumn[j]:
            flag = 1
            result = maxline[i]

if flag == 1:
    print(result[0], result[1])
else:
    print(result)


'''
# 3
# input



s = [int(num) for num in input().split()]
m = s[0]
n = s[1]
lst = []
for i in range(m):
    lsti = [int(num) for num in input().split()]
    lst.append(lsti)
#print(lst)
flag = 0
for i in range(1,m-1):
    for j in range(1,n-1):
        up = lst[i-1][j]
        down = lst[i+1][j]
        left = lst[i][j-1]
        right = lst[i][j+1]
        if lst[i][j] > up and lst[i][j] > down and lst[i][j] > left and lst[i][j] > right:
            print(lst[i][j],i+1,j+1)
            flag = 1
if flag == 0:
    print('None', end=' ')
    print(m, n)



'''
s = [int(num) for num in input().split()]

print('{:>4d}'.format(s[0]), end='')
print('{:>4d}'.format(s[3]), end='')
print('{:>4d}'.format(s[6]) )
print('{:>4d}'.format(s[1]), end='')
print('{:>4d}'.format(s[4]), end='')
print('{:>4d}'.format(s[7]))
print('{:>4d}'.format(s[2]), end='')
print('{:>4d}'.format(s[5]), end='')
print('{:>4d}'.format(s[8]))
'''

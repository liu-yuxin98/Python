# -*- coding: utf-8 -*-
# 2020-03-16
# author Liu,Yuxin
'''

n = int(input())
gradlst = list(map(float, input().split()))
maxgrade = max(gradlst)
mingrade = min(gradlst)
gradlst.remove(maxgrade)
gradlst.remove(mingrade)
# print(gradlst)
avg = sum(gradlst)/(n-2)
print("{:.2f}".format(avg))
'''
'''
x, y = map(int,input().split())
tx, ty = x , y
if x <=y:
    x, y = y, x
while y != 0:
    x, y = y, x%y
gcd = x
lcm = int(tx*ty/gcd)
print(gcd, lcm)
'''

'''
n = int(input())
x = 1
for i in range(1, n):
    x = (x+1)*2
print(x)
'''
'''
n = int(input())
if n == 0:
    print('average = 0.0')
    print('count = 0')
else:
    gradlst = list(map(int, input().split()))
    avg = sum(gradlst)/n
    count = len([i for i in gradlst if i >= 60])
    print('average = ', end='')
    print("{:.1f}".format(avg))
    print('count = '+str(count))
'''
n = 3
m = 4
a = [0] * n
for i in range(n):
    a[i] = [0] * m
    print(a[0][2])
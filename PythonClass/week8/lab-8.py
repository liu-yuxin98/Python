# -*- coding: utf-8 -*-
# 2020-04-15
# author Liu,Yuxin

#1
'''
a,b,c = map(int,input().split())
numset = {3,6,9}
cnt = 0
while True:
    a += 1
    b += 1
    c += 1
    ta = a % 10
    tb = b % 10
    tc = c % 10
    cnt += 1
    result = {ta, tb, tc}
    if cnt >= 100:
        print('so sad!')
        break
    if result == {3, 6, 9}:
        print(cnt)
        break

'''

#2
'''
numstu = int(input().strip())
stulst = [int(i) for i in input().split()]
# print(stulst)
for i in range(0,int(numstu/2)):
    print(str(stulst[i])+" "+str(stulst[-1-i]))

'''


#3
'''
n = int(input())
appleheight = [ int(i) for i in input().split()]
handmax = int(input())
handmax += 30
get = [i for i in appleheight if i<=handmax]
print(len(get))
'''

#4
'''
n = int(input())
nums = [int(i) for i in input().split()]
k = int(input())
indexs = []
for i in range(0,k):
    indexs.append(int(input()))

def remove(nums,x):
    nums = nums[0:x-1]+nums[x::]
    return nums
for i in range(len(indexs)):
    nums = remove(nums,indexs[i])
print(*nums)
'''


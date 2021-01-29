# -*- coding: utf-8 -*-
# 2020-02-03
# author Liu,Yuxin
# entre number:

def insertsort(list):
    for i in range(len(list)-1):
        for j in range(i):
            if list[i]<=list[j]:
                t=list[j]
                list[j]=list[i]
                list[i]=t
    return list

list=[3,4,6,2,1,1,0,7,8,9,11]
insertsort(list)
print(list)


def selectsort(list):
    high=len(list)
    low=0
    while low<high:
        for i in range(low, high):
            if list[i]<=list[low]:
                t=list[low]
                list[low]=list[i]
                list[i]=t
        low+=1
    return list

list=[3,4,6,2,1,1,0,7,8,9,11]
selectsort(list)
print(list)













'''
def binarySearch(list, low, high, key):
    mid=(low+high)//2
    if key == list[mid]:
        return mid
    elif key>list[mid]:
        return binarySearch(list,mid+1,high,key)
    else:
        return binarySearch(list,low,mid-1, key)

l = [x for x in range(1000)]
high=len(l)
print(binarySearch(l, 0, high, 198))
'''




'''
from myOwnfunc import BinarySearch
list1 = [x for x in range(100)]
r=len(list1)
index=BinarySearch.binarySearch(list1, 0, r, 15)
index2=BinarySearch.BinarySearch(15,list1)
print(index)
print(index2)

'''


'''
list=[x for x in range(100)]
z=19
list.sort()
lowIndex=0
highIndex=len(list)-1
low=list[lowIndex]
high=list[highIndex]
midIndex=(highIndex)//2
mid=list[midIndex]
index=1
while low <= high:
    if z > mid:
        lowIndex = midIndex + 1
        low = list[lowIndex]
        midIndex = (lowIndex + highIndex) // 2
    elif z == mid:
        index = midIndex
    else:
        highIndex = midIndex - 1
        high = list[highIndex]
        midIndex = (lowIndex + highIndex) // 2

print(list)
print(index)

'''





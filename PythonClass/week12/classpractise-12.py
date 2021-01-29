# -*- coding: utf-8 -*-
# 2020-04-13
# author Liu,Yuxin
import math
'''
# 0(n^2) 选择排序与冒泡排序性能都比较差,最好的算法可以达到 0（n*log2n)
def bubble(lst, begin, end):
    print(lst)
    if begin < end:
        for i in range(begin, end):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        bubble(lst, begin, end-1)

# 冒泡排序改动，提高性能,减少无用的遍历
def bubble2(lst, begin, end):
    print(lst,end)
    if begin < end:
        lastswapped = -1
        for i in range(begin, end):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                lastswapped = i
        bubble2(lst, begin, lastswapped)

# 创建测试数据
import random
random.seed(2)
lst = []
for i in range(20):
    lst.append(random.randint(0,100))
print(lst)
bubble2(lst, 0, len(lst)-1)
print(lst)
result = True
for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
        result = False
        break
print(result)
'''



# 异常处理
# try-except
s_list = [1,72,3]
position = 6
try:
    s_list[position]
except:
    print('index ∈({},{})'.format(0,len(s_list)-1))

# 内置函数
# sorted 对字符串，列表，元组，字典进行排序， 产生新的一个列表
lst = [ i for i in range(20)]
lst2 = sorted(lst, reverse = True)
print(lst2)
students = [('james',89,15) , ('peter',80,14),('harry',87,16)]
students2 = sorted(students,key=lambda s: s[2])   # 按照年龄排序
students3 = sorted(students, key=lambda s: s[1])  # 按照成绩排序
print(students2)
print(students3)



def bubble(List):
    for j in range( len(List)-1,0,-1):
        for i in range(0,j):
            if List[i]>List[i+1]:
                List[i],List[i+1]=List[i+1],List[i]

    return List

testlist = [49, 38, 65, 97, 76, 13, 27, 49]
print( bubble(testlist))


def selSort(nums):
    n = len(nums)
    for bottom in range(n - 1):
        mi = bottom
        for i in range( mi+1 , n):
            if nums[i] < nums[mi]:
                mi = i
        nums[bottom], nums[mi] = nums[mi], nums[bottom]
    return nums
testlist = [49, 38, 65, 97, 76, 13, 27, 49]
print( selSort(testlist))
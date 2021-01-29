# -*- coding: utf-8 -*-
# 2020-04-01
# author Liu,Yuxin
print(chr(1))

'''

def containsDuplicate(lst):
    s = set(lst) # without set
    if len(s)==len(lst):
        print('NO')
        return 0
    else:
        print('YES')
        return 1

n = int(input())
lst = input().split()
lst = [ int(x) for x in lst]
containsDuplicate(lst)
'''

'''
n = int(input())
lst = input().split()
lst = [ int(x) for x in lst]
lst.sort()
lst = lst[::-1]
print(*lst)
'''
'''
n = int(input())
lst = input().split()
lst = [ int(x) for x in lst]
pen = dict()
for num in lst:
    pen[num] = pen.get(num, 0)+1
for key in pen:
    if pen[key] == 1:
        print(key)
'''


'''
dict1 = dict()
for num in lst: # create dict1
  dict1[num] = dict1.get(num, 0)+1
# print(dict1)
'''



'''
# 方法一
n = int(input())
lst = input().split()
lst = [ int(x) for x in lst]
subset = set(lst)
newset = set()
for i in range(0, len(lst)):
    newset.add(lst[i])
    if newset == subset:
        print(i)
        break
        
#  方法二
n = int(input())
lst = input().split()
lst = [ int(x) for x in lst]
subset = set(lst)
subsetlst = list(subset)
p = lst.index((subsetlst[0]))
for i in range(0, len(subsetlst)):
    if lst.index(subsetlst[i]) >= p:
        p = lst.index(subsetlst[i])

# 方法三
n = int(input())
lst = input().split()
lst = [ int(x) for x in lst]
subset = set(lst)
subsetlst = list(subset)
p = []
for i in range(0, len(subsetlst)):
    p.append(lst.index(subsetlst[i]))  # 找到每个元素第一次出现的下标
print(max(p))

# 方法四
n = int(input())
lst = input().split()
lst = [ int(x) for x in lst]
dict1 = dict()
p = []
for i in range(0, len(lst)):
    dict1[lst[i]] = dict1.get(lst[i], 0)+1
    if dict1[lst[i]] == 1:
        p.append(i)
print(max(p))

'''














# -*- coding: utf-8 -*-
# 2020-02-10
# author Liu,Yuxin
import random
lis = []
for i in range(4):
    lis.append([])
    for j in range(4):
        lis[i].append(random.randint(0,9))

for i in range(4):
    for j in range(4):
        print(lis[i][j],end=' ')
    print('')

countlist = 10*[0]
print(countlist)

for i in range(4):
    for j in range(4):
        num = lis[i][j]
        countlist[num]+=1
print(countlist)





'''

from myOwnfunc import twoD_list as td
lis = td.twoD_list_create(5, 8)

td.twoD_list_print(lis)
numlist = td.twoD_list_create_zero(1, 11)
td.twoD_list_print(numlist)


for i in range(len(lis)):
    for j in range(len(lis[0])):
        numlist[ lis[i][j] ] += 1
td.twoD_list_print(numlist)        


print('------------------------------------')
lis = td.twoD_list_shuffle(lis)
'''


'''
for i in range(len(lis)):
    for j in range(len(lis[0])):
        numlist[lis[i][j]] += 1
        
td.twoD_list_print(numlist)
td.twoD_list_print(lis)
'''



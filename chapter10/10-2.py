# -*- coding: utf-8 -*-
# 2020-02-03
# author Liu,Yuxin
# entre number:
def m(x,lst=None):
    if lst ==None:
        lst=[1,1,2,3,4]
    if x in lst:
        lst.remove(x)
    return lst

list1=m(1)
print(list1)
list2=m(1)
print(list2)
list3=[1,2,3,4,5,1]
list3.remove(1)
print(list3)
'''
list1=[x for x in range(1,10,2)]
print(list1)
print(id(list1))
list2=list1
print(id(list2))
list3=[]+list1
print(id(list3))
list1[0]=14
print(list1)
print(list2)
'''


'''
endOfInput=False
isCovered=99*[False]
allCovered=False

while not endOfInput:
    s = input("enter number:")
    items = s.split()
    list = [eval(x) for x in items]
    for number in list:
        if number == 0:
            endOfInput = True
        else:
            isCovered[number-1] = True
allCovered = True
for i in range(99):
    if isCovered[i] == False:
        allCovered = False
        break

if allCovered:
    print(" all covered")
else:
    print("not all covered ")

'''







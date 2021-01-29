# -*- coding: utf-8 -*-
# 2020-02-20
# author Liu,Yuxin

# create tuple
'''

t1 = ()
t2 = (1, 3, 5)
t3 = tuple([x for x in range(5)])
t4 = tuple('abca')
print(t1)
print(t2)
print(t3)
print(t4)
'''

'''
tuple1 = ('green', 'yellow', 'red')
print(tuple1)
tuple2 = tuple([1,2,3,4,5,6, 9, 10, 8, 0 ])
print(tuple2)
print(len(tuple2))  # len
print(max(tuple2))  # max
print(min(tuple2))  # min
print(sum(tuple2))  # sum
print(tuple2[0])
tuple3 = tuple1 + tuple2
print(tuple3)
tuple3 = 2* tuple1
print(tuple3)
print( 2 in tuple2) # whether 2 is inside tuple2
for v in tuple1:
    print(v, end=" ")
print()
list1 = list(tuple2)
list1.sort()
print(list1)

'''

t1 = ( 0, 6, 9, 1, 5, 2)
list1 = list(t1)
list1.sort()
t1 = tuple(list1)
print(t1)
print(t1[1:-1])
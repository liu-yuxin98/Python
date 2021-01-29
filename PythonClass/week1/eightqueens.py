# -*- coding: utf-8 -*-
def isconflict(state,nextrowpos):
   for column in state:
       if column == nextrowpos: # 列冲突
           return True
   nextrow = len(state) # 下一列是第几列
   for row in range(len(state)):
       if abs(nextrow-row) == abs(state[row]-nextrowpos): # 斜冲突
           return True
   return False
def queens(n,state=[]):
    for pos in range(n):
        if not isconflict(state,pos):
            if len(state) == n-1:
                yield [pos]
            else:
                for result in queens(n,state+[pos]):
                    yield [pos]+result




'''
n = 6
state = [0,2]
nextrowpos = 3
print(isconflict(state,nextrowpos))
'''

def fib(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b



def primelst(n):
    prime = list(range(2,n+1))
    for p in prime:
        for k in range(2*p,n+1,p):
            if k in prime:
                prime.remove(k)
    return prime

print(primelst(100))







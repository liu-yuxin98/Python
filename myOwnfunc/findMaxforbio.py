from myOwnfunc import binomialDistribuation
import math
def findMaxforbio(n,p):
    max=0
    index=0
    for i in range(n+1):
        if binomialDistribuation.binomialDistribuation(i,n,p)>=max:
            max=binomialDistribuation.binomialDistribuation(i,n,p)
            index=i
    return index,max

 # return more than one value x,y=findMaxforbio(195,0.9)
# print(x,y)


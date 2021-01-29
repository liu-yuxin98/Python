#-*-coding:utf-8-*-
import math
from myOwnfunc import combination
def binomialDistribuation(k,n,p):# n次事件中发生k次，其中时间发生的概率是p
    return combination.combination(n,k)*pow(p,k)*pow(1-p,n-k)

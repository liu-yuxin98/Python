#-*-coding:utf-8-*-
import math
from myOwnfunc import combination
def binomialDistribuation(k,n,p):# n���¼��з���k�Σ�����ʱ�䷢���ĸ�����p
    return combination.combination(n,k)*pow(p,k)*pow(1-p,n-k)

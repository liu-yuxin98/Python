import math
from myOwnfunc import factorial

def combination(n,k):
    sum=factorial.factorial(n)/(factorial.factorial(k)*factorial.factorial(n-k))
    return sum

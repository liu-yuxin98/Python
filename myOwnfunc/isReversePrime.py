from myOwnfunc import IsPrime
from myOwnfunc import  Reverse
def isReversePrime(number):
    if number<10:
        return 0
    else:
        if IsPrime.IsPrime(number) and IsPrime.IsPrime(Reverse.reverse(number)):
            return 1
        else:
            return 0



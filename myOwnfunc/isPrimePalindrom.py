from myOwnfunc import isPalindrom
from myOwnfunc import IsPrime

def isPrimPalindrom(number):
    if IsPrime.IsPrime(number) and isPalindrom.isPalindrom(number):
        return 1
    else:
        return 0



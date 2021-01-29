from myOwnfunc import Reverse

def isPalindrom(number):
    if number==Reverse.reverse(number):
        return 1
    else:
        return 0


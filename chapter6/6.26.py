from myOwnfunc import IsPrime
import math
for p in range(1,31):
    if IsPrime.IsPrime(math.pow(2,p)-1):
        print(p,end="  ")
        print(format(math.pow(2,p)-1,"10.0f"))


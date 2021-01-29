from myOwnfunc import IsPrime
for i in range(2,1000):
    if IsPrime.IsPrime(i) and IsPrime.IsPrime(i+2):
        print("("+"{}".format(i,"4.0f")+","+"{}".format(i+2,"4.0f")+")")
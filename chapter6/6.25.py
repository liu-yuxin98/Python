from myOwnfunc import isReversePrime
count=0
for i in range(0,1000):

    if isReversePrime.isReversePrime(i):
        count += 1
        print(format(i,"4.0f"),end="")
        if count%10==0:
            print('\n')





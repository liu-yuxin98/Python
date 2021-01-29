def findFactor(number):
    factor=[]
    sum=0
    i=1
    while i <number:
        if number%i==0:
            factor.append(i)
            sum=sum+i
        i+=1
    return sum

for i in range(1,10000):
    if i==findFactor(i):
        print(i)


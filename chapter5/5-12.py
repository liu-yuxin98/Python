def isPrime(x):
 if(x==1):
     return 0
 elif x==2:
     return 1
 else:
     i=2
     while i<x:
         if(x%i==0):
             return 0
         i=i+1
     if(i==x):
         return 1



count=0
i=0
while count<50:
    if(isPrime(i)==1):
        print(format(i,"5d"), end=" ") #¶ÔÆë
        count += 1
        if count%10==0:
            print(" ")
    i=i+1



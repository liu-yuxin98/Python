import math
sum=1
for i in range(1,1000):
    sum+=1/math.factorial(i)
print(format(sum,"10.6f"))
print(format(math.e,"10.6f"))
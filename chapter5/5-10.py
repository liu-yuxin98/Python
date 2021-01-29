import random
num=1000000
count=0
for i in range(0,num):
    x = random.random()
    y = random.random()
    if x*x+y*y<=1:
        count+=1
print(4*count)
print(4*count/num)

import random
num=[]
for i in range(0,5):
    num.append(random.randint(-10,10))
for i in range(0,5):
    print(num[i])
print(" ")

for i in range(0,4):
    if num[i+1]>=num[i]:
        t=num[i]
        num[i]=num[i+1]
        num[i+1]=t

for i in range(0,5):
    print(num[i])

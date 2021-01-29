import random
num1=random.randint(0,100)
num2=random.randint(0,100)
print(num1,num2)
t=0
if num1<num2:
   t=num1
   num1=num2
   num2=t
print("what is num1-num2:")
answer=eval(input("enter your answer"))
if answer==num1-num2:
    print("correct")
else:
    print("wrong")
count=eval(input("enter count"))
print(bool(count%10==0))
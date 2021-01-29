import time
import random
correct=0
t1=time.time()
for i in range(0,3):
    num1 = random.randint(0, 16)
    num2 = random.randint(0, 16)
    operator = random.randint(0, 2)
    if(operator==0):
        print("{}+{}=".format(num1,num2))
        anwser=eval(input("enter your answer:"))
        if anwser==num1+num2:
            correct+=1
        else:
            print("wrong!")
    else:
        print("{}-{}=".format(num1, num2))
        anwser = eval(input("enter your answer:"))
        if anwser == num1 - num2:
            correct += 1
        else:
            print("wrong!")

t2=time.time()
print("you spend",end=" ")
print(format(t2-t1,"5.2f"))
print("seconds")
print("you are correct {} times".format(correct))
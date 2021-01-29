import random
num1=eval(input("enter your guess number range from [10,99]:"))
num1_a=num1%10
num1_b=num1//10
num2=random.randint(10,100)
num2_a=num2%10
num2_b=num2//10
print(num2)
if num1==num2:
    print("you get 100")
elif((num1_a==num2_a or num1_a==num2_b) and(num2_b==num2_a or num2_b ==num2_a)):
    print(" you get 30")
elif (num1_a==num2_a or num1_a==num2_b) or (num2_b==num2_a or num2_b ==num2_a):
    print(" you get 10")
else:
    print("you get nothing")
import random
for i in range(0,100):
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    while num2 == num1:
        num2 = random.randint(1, 9)
    print(num1, end="")
    print(num2, end=" ")
    if i% 10==0:
        print(" ")



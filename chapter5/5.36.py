import random

win_cpu=0
win_user=0

while win_cpu!=2 and win_user!=2:
    print("scissor(1),rock(2),paper(3)")
    num1 = random.randint(1, 3)
    num2 = eval(input("enter your choice:"))
    if num2 == 1:
        if (num1 == 1):
            print(" same scissor")
        elif num1 == 2:
            print(" cpu->rock, you lose")
            win_cpu += 1
        else:
            print("cpu->paper, you win")
            win_user += 1
    elif num2 == 2:
        if (num1 == 1):
            print(" cpu->scissor, you win")
            win_user += 1
        elif num1 == 2:
            print(" same rock")
        else:
            print("cpu->paper, you lose")
            win_cpu += 1
    else:
        if (num1 == 1):
            print(" cpu->scissor, you lose")
            win_cpu += 1
        elif num1 == 2:
            print(" cpu->rock, you win")
            win_user += 1
        else:
            print("same paper")





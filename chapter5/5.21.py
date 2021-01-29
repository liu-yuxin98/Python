import math
numberOfline=eval(input("enter th enumber of lines:"))
for i in range(1,numberOfline+1):
    for k in range(0,numberOfline-i):
        print("    ",end="")
    for j in range(0, i):
        print(format(math.pow(2, j), "4.0f"), end="")
    j = j - 1
    while j >= 0:
        print(format(math.pow(2, j), "4.0f"), end="")
        j -= 1
    print(" ")


number=eval(input("enter the number of lines:"))
i=1
while i<=number:
    j = i
    for k in range(0,2*(number-i)):
        print(" ",end="")
    while j > 0:
        print(j, end=" ")
        j -= 1
    j = j + 2
    while j < i+1:
        print(j, end=" ")
        j += 1
    i+=1
    print(" ")





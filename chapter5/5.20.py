numberOfline=eval(input("enter the number of lines:"))
#A
for i in range(1,numberOfline+1):
    j=i
    for j in range(1,i+1):
        print(j,end=" ")
    print(" ")
# divide
for i in range(0,15):
    print("-", end=" ")
print(" ")

#B
i=numberOfline
while i>=1:
    for j in range(1,i+1):
        print(j,end=" ")
    print(" ")
    i-=1

# divide
for i in range(0, 15):
    print("-", end=" ")
print(" ")
#C
i=1
while i<=numberOfline:
    j=i
    # blank
    for k in range(0,(numberOfline-j)*2):
        print(" ",end="")
    #number
    while j>=1:
        print(j,end=" ")
        j-=1
    # next line
    print(" ")
    i+=1
# divide
for i in range(0, 15):
    print("-", end=" ")
print(" ")
#D
i=1
while i<=numberOfline:
    for k in range(0,2*(i-1)):
        print(" ",end="")
    for j in range(1,numberOfline+2-i):
        print(j,end=" ")
    print(" ")
    i+=1
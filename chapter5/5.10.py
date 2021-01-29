import os
from prettytable import PrettyTable
x=PrettyTable(["name","score"])
numberOfstudents=eval(input("number of students:"))
name=[]
score=[]
for i in range(0,numberOfstudents):
    name.append(input(" enter student's name:"))
    score.append(eval(input("his score:")))
max=score[0]
maxName=name[0]
for i in range(0,numberOfstudents):
    if(score[i]>=max):
        max=score[i]
        maxName=name[i]

for i in range(0,numberOfstudents):
    x.add_row([name[i],score[i]])

print(x)
print(maxName,end=" ")
print("has highest score:",end=" ")
print(max)

os.system(" python 5.10.py > 5.10-output.txt")



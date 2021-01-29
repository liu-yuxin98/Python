import random
import turtle
import time
#draw 20*20 grid
turtle.speed(100)
turtle.color('gray')
for i in range(-100,110,10):
    turtle.penup()
    turtle.goto(i,100)
    turtle.pendown()
    turtle.goto(i,-100)

for j in range(-100,110,10):
    turtle.penup()
    turtle.goto(-100,j)
    turtle.pendown()
    turtle.goto(100,j)
turtle.penup()
i=0
j=0
turtle.goto(i,j)
turtle.color("red")
turtle.pensize(3)
turtle.speed(1)
turtle.pendown()

while (i!=-10 and i!=10) and(j!=-10 and j!=10):
    k=random.randint(0,2)
    if k==0:
        i = i + random.randint(-1, 2)
    else:
        j = j + random.randint(-1, 2)

    turtle.goto(10 * i, 10 * j)


turtle.done()
time.sleep(10)
'''
for i in range(0,51):
    x=random.randint(0,3)
    if x==0:
        turtle.left(90)
        turtle.forward(10)

    elif x==1:
        turtle.right(90)
        turtle.forward(10)

    else :
        turtle.forward(10)

'''





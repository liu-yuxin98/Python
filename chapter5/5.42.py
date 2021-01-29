import random
import turtle
import time
t1=time.time()

turtle.speed(90000)
turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()
turtle.goto(-100,100)
turtle.goto(100,100)
turtle.goto(100,-100)
turtle.goto(-100,-100)
turtle.penup()
turtle.goto(0,100)
turtle.pendown()
turtle.goto(0,-100)
turtle.goto(0,100)
turtle.goto(100,0)
turtle.goto(0,0)
turtle.penup()
turtle.goto(-50,0)
turtle.pendown()
turtle.write("1")
turtle.penup()
turtle.goto(25,25)
turtle.pendown()
turtle.write("3")
turtle.penup()
turtle.goto(75,50)
turtle.pendown()
turtle.write("2")
turtle.penup()
turtle.goto(50,-50)
turtle.pendown()
turtle.write("4")
count=0
num=50
turtle.speed(90000)
for i in range(0,num):
    turtle.penup()
    x=100*(random.random()*2-1)
    y=100*(random.random()*2-1)
    if x<=0:
        count+=1
    elif y>=0 and x+y<=100:
        count+=1
    else:
        count=count
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(1)
    turtle.end_fill()
turtle.penup()
turtle.goto(0,200)
turtle.pendown()
turtle.write(count/num)
t2=time.time()
turtle.penup()
turtle.goto(0,300)
turtle.pendown()
turtle.write(t2-t1)
print(t2-t1)


turtle.done()
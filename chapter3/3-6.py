import turtle
import time
turtle.pensize(5)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.begin_fill()
turtle.color("yellow")
turtle.circle(40)
turtle.end_fill()
turtle.color("blue")
turtle.circle(45)
turtle.circle(80,steps=6)
turtle.done()
time.sleep(10)
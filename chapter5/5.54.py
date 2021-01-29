import turtle

for i in range(-100,100,1):
    turtle.speed(1000)
    turtle.penup()
    turtle.goto(i,1/100*i*i)
    turtle.pendown()
    turtle.goto(i+1,1/100*(i+1)*(i+1))
turtle.done()
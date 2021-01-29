import turtle
turtle.penup()
turtle.speed(200)
# draw squares
for j in range(0,90,10):
    turtle.goto(0,j)
    turtle.pendown()
    turtle.goto(80,j)
    turtle.penup()
for i in range(0,90,10):
    turtle.penup()
    turtle.goto(i,0)
    turtle.pendown()
    turtle.goto(i,80)
    # draw black squares
turtle.speed(200)
for i in range(0,80,10): # every column
    for j in range(0,80,20): # every line
        if i%20==0: # column number is odd:1,3,5,7
            turtle.penup()
            turtle.fillcolor("black")
            turtle.begin_fill()
            turtle.goto(i, j)
            turtle.pendown()
            turtle.goto(i,j+10)
            turtle.goto(i+10,j+10)
            turtle.goto(i+10,j)
            turtle.goto(i,j)
            turtle.end_fill()
        else: # column number is even:2,4,6,8
            turtle.penup()
            turtle.fillcolor("black")
            turtle.begin_fill()
            turtle.goto(i, j+10)
            turtle.pendown()
            turtle.goto(i, j + 20)
            turtle.goto(i + 10, j + 20)
            turtle.goto(i + 10, j+10)
            turtle.goto(i, j+10)
            turtle.end_fill()
turtle.done()


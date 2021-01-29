import turtle
def drawCircle(x=0,y=0,r=100): #(x,y) r
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(r)
    turtle.done()
def drawRectangle(x=0,y=0,width=100,length=200):
    turtle.penup()
    turtle.goto(x-length/2,y-width/2)
    turtle.pendown()
    turtle.goto(x-length/2,y+width/2)
    turtle.goto(x+length/2,y+width/2)
    turtle.goto(x+length/2,y-width/2)
    turtle.goto(x-length/2,y-width/2)

def writeText(s,x=0,y=0):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.write(s)


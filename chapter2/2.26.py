import turtle

(x1,y1)=eval(input("enter center of the round in the form of (x,y):"))
radius=eval(input("enter radius:"))
area=3.1415926*radius*radius
turtle.goto(x1,y1)
turtle.pendown()
turtle.write("the area of the circle is{}".format(area))
turtle.penup()
turtle.goto(x1, y1 - radius)
turtle.pendown()
turtle.circle(radius)
turtle.done()


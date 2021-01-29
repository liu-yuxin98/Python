import turtle
import math
import time
r=eval(input("enter r:"))
turtle.circle(r)
turtle.circle(r,steps=5)
area=5*math.pow((2*r*math.sin(math.pi/5)),2)/(4*math.tan(math.pi/5))

turtle.goto(0,r/2)

turtle.write("area is{}".format(area,"10.2f"))
turtle.done()
time.sleep(10)
'''
        Polygon
___________________________
-n:int>=3
-side:float
-x:float
-y:float
___________________________
Polygon(n:int,side:float,x:float,y:float)
getN()
getSide()
getX()
getY()
setN()
setSide()
setX()
setY()
getPerimeter()
getArea(): n*pow(s,2)/(4*tan(pi/n)
Draw()

'''
import turtle
import math
import random
class Polygon:
    def __init__(self,n=3,side=50,x=0,y=0):
        self.__n=n
        self.__side=side
        self.__x=x
        self.__y=y
    def getN(self):
        return self.__n
    def getSide(self):
        return self.__side
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def setN(self,n):
        self.__n=n
    def setSide(self,side):
        self.__side=side
    def setX(self,x):
        self.__x=x
    def setY(self,y):
        self.__y=y
    def getPerimeter(self):
        return self.__n*self.__side
    def getArea(self):
        return self.__n*math.pow(self.__side,2)/(4*math.tan(math.pi/self.__n))
    def Draw(self):
        n=self.__n
        side=self.__side
        x=self.__x
        y=self.__y
        angle1=360/(2*n)
        angle2=180-180*(n-2)/n
        turtle.penup()
        turtle.goto(x,y)
        turtle.penup()
        turtle.left(angle1)
        turtle.speed(500)
        turtle.forward(side/2/math.sin(angle1))
        turtle.pendown()
        turtle.left(90+angle1)
        for i in range(n):
            turtle.forward(side)
            turtle.right(angle2)

'''
test1
p1=Polygon()
p1.Draw()
p2=Polygon(4)
p2.Draw()
P3=Polygon(5,100)
P3.Draw()
'''

'''
test2
p=[]
for i in range(20):
   #p.append(Polygon())
    p.append(Polygon(random.randint(3,10),random.randint(30,60),random.randint(-50,50),random.randint(-50,50)))
    p[i].Draw()
'''



#-*- coding=utf-8-*-
import math
class Circle:
    def __init__(self,radius=1):
        self.radius=radius
    def getPerimeter(self):
        return self.radius*2*math.pi
    def getArea(self):
        return self.radius*self.radius*math.pi
    def setRadius(self,radius):
        self.radius=radius

class Rectangular:
    def __init__(self,length=2,width=1):
        self.width=width
        self.length=length

    def setLength(self, length):
        self.length=length
    def setWidth(self, width):
        self.width=width
    def getArea(self):
        return self.width*self.length
    def getPerimeter(self):
        return 2*(self.width+self.length)

class Coordinate:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def setVaule(self,x,y):
        self.x=x
        self.y=y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
'''
c1=Circle()# c1.radius=1 
print(c1.radius)
r1=Rectangular(5,3)
print(r1.getArea())
p1=Coordinate(5,6)
print(p1.x)
print(p1.getX())
'''


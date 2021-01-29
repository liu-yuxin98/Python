#-*- coding=utf-8-*-
import math
'''
from chapter7 import shape

myCircle=shape.Circle()
print(myCircle.radius)
myCircle.setRadius(5)
print(myCircle.radius)
'''
class Circle:
    def __init__(self,radius=1):
        self.radius=radius
    def getPerimeter(self):
        return self.radius*2*math.pi
    def getArea(self):
        return self.radius*self.radius*math.pi
    def setRadius(self,radius):
        self.radius=radius

def main():
    myCircle=Circle()
    n=5
    printAreas(myCircle,n)

    print('\nRadius is',myCircle.radius)
    print("n is",n)

def printAreas(c,times):
    print("Radius\t\tArea")
    while times>=1:
        print(c.radius,"\t\t",c.getArea())
        c.radius=c.radius+1
        times=times-1

main()



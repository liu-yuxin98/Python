'''
        endPoint
______________________
-p1:Point
-p2:Point
-p3:Point
-p4:Point
______________________
endPoint(p1,p2,p3,p4): create
getLine1(p1,p2): PointToLine(p1,p2)->get a,b,c
getLine2(p3,p4): PointToLine(p3,p4)->get d,e,f
getEndPoint(): LingerEquation(a,b,c,d,e,f)->x,y
'''
from chapter7 import LingerEquation
from chapter7 import Point
from chapter7 import PointToLine
class endPoint:
    def __init__(self,p1,p2,p3,p4,a=0,b=0,c=0,d=0,e=0,f=0):
        self.__p1=p1
        self.__p2=p2
        self.__p3=p3
        self.__p4=p4
        self.__a=a
        self.__b=b
        self.__c=c
        self.__e=e
        self.__f=f
    def getP1(self):
        return self.__p1
    def getP2(self):
        return self.__p2
    def getP3(self):
        return self.__p3
    def getP4(self):
        return self.__p4
    def getLine1(self):
        self.__a,self.__b,self.__e=PointToLine.PointToLine(self.__p1,self.__p2)
        return self.__a,self.__b,self.__e
    def getLine2(self):
        self.__c,self.__d,self.__f=PointToLine.PointToLine(self.__p3,self.__p4)
        return self.__c,self.__d,self.__f
    def getEndPoint(self):
        self.getLine1()
        self.getLine2()
        a=self.__a
        b=self.__b
        c=self.__c
        d=self.__d
        e=self.__e
        f=self.__f
        r=LingerEquation.LingerEquation(a,b,c,d,e,f)
        return r.getX(),r.getY()
p1=Point.Point(0,0)
p2=Point.Point(1,1)
p3=Point.Point(1,0)
p4=Point.Point(2,-1)
endPoint1=endPoint(p1,p2,p3,p4)
x,y=endPoint1.getEndPoint()
print(x)
print(y)

'''
            Line
_________________
-a:float
-b: float
-c:float
_________________
Line(a:float , b:float , c:float)
seta()
setb()
setc()
geta()
getb()
getc()

'''
class Line:
    def __init__(self,a,b,c):
        self.__a=a
        self.__b=b
        self.__c=c
    def seta(self,a):
        self._a=a
    def setb(self,b):
        self.__b=b
    def setc(self,c):
        self.__c=c
    def geta(self):
        return self.__a
    def getb(self):
        return self.__b
    def getc(self):
        return self.__c

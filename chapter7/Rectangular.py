class Rectangular:
    def __init__(self,width=10,length=20):
        self.__width=width
        self.__length=length
    def setWidth(self,width):
        self.__width=width
    def setLength(self,length):
        self.__length=length
    def getWidth(self):
        return self.__width
    def getLength(self):
        return self.__length
    def getArea(self):
        return self.__length*self.__width
    def getPrimiter(self):
        return 2*(self.__width+self.__length)

#r1=Rectangular(5,10)
#print(r1.getArea())
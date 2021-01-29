'''
ax+by=e
cx+dy=f
            LingerEquation
__________________________________
-a:float
-b:float
-c:float
-d:float
-e:float
-f:float
___________________________________
LingerEquation()
geta()
getb()
...
isSolvable()   if ad-bc!=0: true
getX()
getY()
'''
class LingerEquation:
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f
    def geta(self):
        return self.__a
    def getb(self):
        return self.__b
    def getc(self):
        return self.__c
    def getd(self):
        return self.__d
    def gete(self):
        return self.__e
    def getf(self):
        return self.__f
    def isSolvable(self):
        ad=self.geta()*self.getd()
        bc=self.getb()*self.getc()
        if ad-bc==0:
            return False
        else:
            return True
    def getX(self):
        a=self.geta()
        b=self.getb()
        c=self.getc()
        d=self.getd()
        e=self.gete()
        f=self.getf()
        if self.isSolvable()==True:
            return (e*d-b*f)/(a*d-b*c)
        else:
            return "can't solve"
    def getY(self):
        a = self.geta()
        b = self.getb()
        c = self.getc()
        d = self.getd()
        e = self.gete()
        f = self.getf()
        if self.isSolvable()==True:
            return (a*f-e*c)/(a*d-b*c)
        else:
            return " can't solve"
'''
le1=LingerEquation(1,-1,1,1,-1,1)
x=le1.getX()
y=le1.getY()
print(x,y)
'''





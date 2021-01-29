# encoding=utf-8
'''
        Rational
____________________
-numerator:int
-denominator:int
________________________
Rational(numerator:int,denominator:int)
__add__( secondRational:Rational) [ find smallest common 倍数   LCM]
__sub__(secondRational:Rational)
__mul__(secondRational:Rational)
__truediv__(secondRational:Rational) #除法
__lt__(secondRational:Rational) #比较大小
__int__():int
__float__():float
___________________________________
'''
from myOwnfunc import leastCommonMultiple
class Rational:
    def __init__(self,num,denum):#denum!=0
        self.__num = num
        self.__denum=denum
    def __add__(self,secondRational):
        if self.__denum>0 and secondRational.__denum>0:#两个有理数的分母都大于零
            lcm=leastCommonMultiple.lcm(self.__denum,secondRational.__denum) # find lcm for denum
            self.__num=self.__num*lcm/self.__denum # 通分，第一个有理数的分子
            secondRational.__num=secondRational.__num*lcm/secondRational.__denum # 通分，第二个有理数的分子
            result=self #结果
            result.__num=self.__num+secondRational.__num
            result.__denum=lcm
        elif self.__denum<0 and secondRational.__denum>0:#两个中第一个的分母为负数
            self.__denum=-self.__denum
            lcm=leastCommonMultiple.lcm(self.__denum,secondRational.__denum)
            self.__num = -self.__num * lcm / self.__denum  # 通分，第一个有理数的分子
            secondRational.__num = secondRational.__num * lcm / secondRational.__denum  # 通分，第二个有理数的分子
            result = self  # 结果
            result.__num = self.__num + secondRational.__num
            result.__denum = lcm
        elif self.__denum<0 and secondRational.__denum<0:#两个的分母为负数
            self.__denum=-self.__denum
            secondRational.__denum=-secondRational.__denum
            lcm=leastCommonMultiple.lcm(self.__denum,secondRational.__denum)
            self.__num = -self.__num * lcm / self.__denum  # 通分，第一个有理数的分子
            secondRational.__num = -secondRational.__num * lcm / secondRational.__denum  # 通分，第二个有理数的分子
            result = self  # 结果
            result.__num = self.__num + secondRational.__num
            result.__denum = lcm
        else:#第二个为负数
            secondRational.__denum = -secondRational.__denum
            lcm = leastCommonMultiple.lcm(self.__denum, secondRational.__denum)
            self.__num = self.__num * lcm / self.__denum  # 通分，第一个有理数的分子
            secondRational.__num = -secondRational.__num * lcm / secondRational.__denum  # 通分，第二个有理数的分子
            result = self  # 结果
            result.__num = self.__num + secondRational.__num
            result.__denum = lcm
        return result
    def __sub__(self,secondRational):
        secondRational.__num=-secondRational.__num
        result=self.__add__(secondRational)
        return result
    def __mul__(self,secondRational):
        result=self
        result.__num=self.__num*secondRational.__num
        result.__denum=self.__denum*secondRational._denum
        return result
    def __truediv__(self,secondRational):
        result=self
        result.__num=self.__num*secondRational._denum
        result.__denum=self.__denum*secondRational.__num
        return result
    def __lt__(self,secondRational):
        result=self.__sub__(secondRational)
        temp=result.__denum * result.__num
        if(temp>0):
            self.__show__()
            print(">")
            secondRational.__show__()
            return 1
        elif temp==0:
            self.__show__()
            print("=")
            secondRational.__show__()
            return 0
        else:
            self.__show__()
            print("<")
            secondRational.__show__()
            return -1
    def __int__(self):
        result=round(self.__num/self.__denum)
        print(result,int)
    def __float__(self):
        result=self.__num/self.__denum
        print(format(result,".5f"))
    def __show__(self):
        print(format(self.__num,".0f"),"/ ",format(self.__denum,".0f"))
'''
r1=Rational(-2,3)
r2=Rational(4,-5)
r1.__show__()
r2.__show__()
r3=r1.__add__(r2)
r3.__show__()
r3=r1.__sub__(r2)
r3.__float__()
r3.__show__()

'''







# -*- coding: utf-8 -*-
# 2020-04-13
# author Liu,Yuxin
# 封装
'''

封装
将数据和对数据的操作组合起来构成类，类是一个不可分割的独立单位。
类中既要提供与外部联系的借口，也需要隐藏细节
python类中成员分为数据成员和方法成员
接口
Python 类中成员：
    数据成员
        类数据成员
        实例数据成员
            公有
            内部： '__'
    方法
        实例方法：公有
                 私有  '__'
        类方法：
        静态方法

python 中以下划线开头的有特殊含义

类成员变量与实例成员变量


class A:
    def __init__(self):
        self.x = 1
        self.__y = 1
    def get(self):
        return self.__y

class Point:
    zero = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def prt(self):
        print(Point.zero, self.zero, self.x,self.y)
p1 = Point(1,2)
p2 = Point(3,4)
p1.zero = 100

p1.prt()
print(p1.x,p1.y,p1.zero)
print(Point.zero)
print(Point.x)  # 错的  zero 是 Point的
# 类成员变量（类变量zero,属于类，不是属于具体的某一个对象），访问类变量可以 类.类变量 对象.类变量

Point.zero = 10
p2.prt()
p1.prt()
# 继承


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, v2): # add
        r = Vector # 也可以 Vector(0,0,0)
        r.x = self.x + v2.x
        r.y = self.y + v2.y
        r.z = self.z + v2.z
        return r
    def show(self):
        print('({}, {}, {})'.format(self.x, self.y, self.z))

v1 = Vector(1,2,3)
v2 = Vector(4,5,6)
v3 = v1+v2
v1.show()
Vector.show(v3)



'''
class A():
    count = 0
    def __init__(self):
        A.count += 1
    def claim(self):
        print('i am a')
    @classmethod
    def kids(cls):
        print(cls.count)
    @staticmethod
    def comme():
        print('this adv')
a1 = A()
a2 = A()
a3 = A()
A.kids()
A.comme()


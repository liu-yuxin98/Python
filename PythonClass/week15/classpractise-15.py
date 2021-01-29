# -*- coding: utf-8 -*-
# 2020-04-13
# author Liu,Yuxin
'''
面相对象的概念
物件导向
对象
构造器，构造list类的对象


'''
'''
s = ['cc','bbb','ads','sss','bbb','cc']
# 保持顺序不变删除重复项
add_to = list(set(s))
print(add_to)
print(list.index(s,'cc'))
add2 = list(set(s))
add2.sort(key = s.index)
print(add2)

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,r):
        v = Vector(self.x + r.x,self.y + r.y)
        return v
    def show(self):
        print(self.x,self.y)
v1 = Vector(1,2)
v2 = Vector(5,6)
v1+v2
v1.show()
v3 = v1+v2
v3.show()
# add 与show 函数的区别
'''
class A:
    def __init__(self):
        self.i = 1

    def m(self):
        self.i = 10

class B(A):
    def m(self):
        self.i += 1
        return self.i


def main():
    b = B()
    print(b.m())

main()

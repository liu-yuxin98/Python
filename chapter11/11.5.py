# -*- coding: utf-8 -*-
# 2020-02-10
# author Liu,Yuxin
import random
import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
Pointlist = []

def Distance(Point1, Point2):
    x = math.fabs(Point1.x-Point2.x)
    y = math.fabs(Point1.y-Point2.y)
    d = math.sqrt(math.pow(x, 2)+math.pow(y, 2))
    round(d, 2)
    return d

for i in range(5):
    Pointlist.append(Point(random.randint(-5, 5), random.randint(-5, 5)))

DistanceMatrix = []

for i in range(5):
    DistanceMatrix.append([])
    for j in range(5):
        distance = Distance(Pointlist[i], Pointlist[j])
        DistanceMatrix[i].append(distance)

for i in range(5):
    print("{}  ( {} , {} )".format(i, Pointlist[i].x, Pointlist[i].y))

for i in range(5):
    for j in range(5):
        print('%.2f' % DistanceMatrix[i][j], end=' ')
    print(' ')

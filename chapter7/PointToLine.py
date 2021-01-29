from chapter7 import Point

def PointToLine(p1,p2):
    x1=p1.getX()
    y1=p1.getY()
    x2=p2.getX()
    y2=p2.getY()
    if x1-x2==0:
        b=0
        a=1
        c=x1
    else:
        a=(y2-y1)/(x2-x1)
        b=-1
        c=a*x1-y1
    return a,b,c
'''
p1=Point.Point(0,0)
p2=Point.Point(1,1)
print(PointToLine(p1,p2))

p3=Point.Point(1,0)
p4=Point.Point(2,-1)
a,b,c=PointToLine(p3,p4)
print(a,b,c)
'''




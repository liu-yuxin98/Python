import math
import turtle
x1,y1=eval(input("enter the center of the first rectangular:(x1,y1)="))
width1=eval(input("enter the width of the first rectangular:"))
length1=eval(input("enter the length of the first rectangular"))
x2,y2=eval(input("enter the center of the second rectangular:(x1,y1)="))
width2=eval(input("enter the width of the second rectangular:"))
length2=eval(input("enter the length of the second rectangular"))
# 4 points of A
a1=[x1-width1/2,y1+length1/2]
a2=[x1+width1/2,y1+length1/2]
a3=[x1+width1/2,y1-length1/2]
a4=[x1-width1/2,y1-length1/2]
# 4points of B
b1=[x2-width2/2,y2+length2/2]
b2=[x2+width2/2,y2+length2/2]
b3=[x2+width2/2,y2-length2/2]
b4=[x2-width2/2,y2-length2/2]

# Whether a point is inside a rectangular
def isInside(x2,y2,width2,length2,a=[]):
    if ((x2 + width2 / 2) >= a[0] >= (x2 - width2 / 2) and (y2 - length2 / 2) <= a[1] <= (y2 + length2 / 2)):
        return 1 # inside
    else:
        return 0 # outside
# count how many points of A is inside of B
counta=isInside(x2,y2,width2,length2,a1)+isInside(x2,y2,width2,length2,a2)+isInside(x2,y2,width2,length2,a3)+\
      isInside(x2,y2,width2,length2,a4)
if( counta==0):
    print("A is outside B")
elif counta==1:
    print("A has one point inside B")
elif counta==2:
    print("A has tow points inside B")
else:
    print('A is inside B')

# count how many points of B is inside A
countb=isInside(x1,y1,width1,length1,b1)+isInside(x1,y1,width1,length1,b2)+isInside(x1,y1,width1,length1,b3)+\
       isInside(x1,y1,width1,length1,b1)
if( countb==0):
    print("B is outside A")
elif countb==1:
    print("B has one point inside A")
elif countb==2:
    print("B has tow points inside A")
else:
    print('B is inside A')

# draw two rectangular
turtle.penup()
turtle.goto(x1-width1/2,y1+length1/2)
turtle.pendown()
turtle.goto(x1+width1/2,y1+length1/2)
turtle.goto(x1+width1/2,y1-length1/2)
turtle.goto(x1-width1/2,y1-length1/2)
turtle.goto(x1-width1/2,y1+length1/2)
turtle.penup()
turtle.goto(x2-width2/2,y2+length2/2)
turtle.pendown()
turtle.goto(x2+width2/2,y2+length2/2)
turtle.goto(x2+width2/2,y2-length2/2)
turtle.goto(x2-width2/2,y2-length2/2)
turtle.goto(x2-width2/2,y2+length2/2)
turtle.done()








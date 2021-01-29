import math
x1,y1=eval(input("(x1,y1)="))
a=eval(input("enter side length of bigger square a"))
x2,y2=eval(input("(x2,y2)="))
b=eval(input("enter side length of smaller square b"))
w1=math.fabs(x1-x2)
w2=math.fabs(y1-y2)
if w1>(a+b)/2 or w2>(a+b)/2:
    print("outside")
else:
    print("have overlap")
    if w1+b/2<a/2 and w2+b/2<a/2:
        print(" total overlap")
    else:
        print("partial overlap")


import math
import random
a=random.randint(0,100)
b=random.randint(0,100)
c=random.randint(0,100)
print("a={}".format(a),end=" ")
print("b={}".format(b),end=" ")
print("c={}".format(c))
print("{}x^2+{}x+{}=0".format(a,b,c))
delt=b*b-4*a*c
print("delt={}".format(delt))
x1=x2=0
if delt>=0:
    x1=(-b+math.sqrt(delt))/(2*a)
    x2=(-b-math.sqrt(delt))/(2*a)
    print("x1={},x={}".format(x1,x2))
else:
    print("the equation has no real roots")



import math
x1,y1=eval(input("enter latitude and longitude for first point"))
x2,y2=eval(input("enter latitude and longitude for second point"))
x1=math.radians(x1)
x2=math.radians(x2)
y1=math.radians(y1)
y2=math.radians(y2)
d=6371*math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
print("distance={}".format(d))
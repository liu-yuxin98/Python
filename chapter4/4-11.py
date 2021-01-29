#-*-coding:utf-8-*-
import random
def isLeapyear( year ):
 print("判断{}是否为闰年".format(year))
 if(year%4==0 and year%100!=0):
    print("{}is leap year".format(year))
    return(1)
 elif(year%400==0):
    print("{}is leap year".format(year))
    return(1)
 else:
    print("{}isn't leap year".format(year))
    return(0)

month_1=[31,28,31,30,31,30,31,31,30,31,30,31]
month_2=[31,29,31,30,31,30,31,31,30,31,30,31] #leap  year
year=eval(input("enter a year:"))
month=eval(input("enter a month:"))
if isLeapyear(year)==1:
    print(month_2[month-1])
else:
    print(month_1[month-1])

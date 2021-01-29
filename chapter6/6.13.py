#-*-coding:utf-8-*-
from myOwnfunc import IsLeapYear
from prettytable import PrettyTable





def PrintTitle(year,month):
    IsLeapYear.GetMonth(month)
    print("{}".format(year))
    print('-------------------------------------')
    print(" "+"SUN"+" "+"MON"+" "+"TUE"+" "+"WED"+" "+"THU"+" "+"FRI"+" "+"SAT")

def PrintMonth(year,month):
    day = IsLeapYear.DayInWeek(year, month, 1)# month的第一天是周几
    NumberOfDay = IsLeapYear.NumberOfDaysOftheMonth(year, month) #这个月一共有几天

    if day==7:
        print("",end="")
    else:
        for i in range(0,day):
            print("    ",end="")  # print the blanket before first day of the month
    for i in range(1,NumberOfDay+1):
        print(format(i,"3.0f"),end=" ")
        if i==7-day:
            print("")
        elif i>7 and (i-1-day)%7==0: # change to next line
            print("")






def main():
    year = eval(input("enter year:"))
    month = eval(input("enter month 1->12:"))
    PrintTitle(year,month)
    PrintMonth(year,month)

main()

def IsLeapYear(year):
      if year%4==0 and year%100!=0:
        return 1
      elif year%400==0:
          return 1
      else:
          return 0
monthLeap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def NumberOfDaysOftheMonth(year,month):
    if IsLeapYear(year):
        return monthLeap[month-1]
    else:
        return month[month-1]
#1800 year 1.1 is Wednesday
def DayInWeek(year,month,day): # return the  day  in a week
    sum=0
    for i in range(1800,year):
        if IsLeapYear(i):
            sum+=366
        else:
            sum+=365

    if IsLeapYear(year):
        for j in range(0,month):
            sum+=monthLeap[j]
    else:
        for j in range(0,month):
            sum+=month[j]
    sum+=day-1
    day=sum%7
    return day

def GetMonth(n):
    if n==1:
        print("Jan",end=" ")
    elif n==2:
        print("Feb",end=" ")
    elif n==3:
        print("Mar",end=" ")
    elif n==4:
        print("April",end=" ")
    elif n==5:
        print("May",end=" ")
    elif n==6:
        print("June",end=" ")
    elif n==7:
        print("July",end=" ")
    elif n==8:
        print('Aug',end=" ")
    elif n==9:
        print("Sept",end=" ")
    elif n==10:
        print("Oct",end=" ")
    elif n==11:
        print("Nov",end=" ")
    else:
        print("Dec",end=" ")









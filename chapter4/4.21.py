
year=eval(input("enter a year:(e.g.,2008):"))
month=eval(input("enter a month:1-12:"))
day=eval(input("enter a day:1-31:"))
h=(day+(26*(month+1)/10)+year%100+(year%100)/4+year/100+5*(year/100))%7
if h==1:
    print("monday")
elif h==2:
    print("tuesday")
elif h==3:
    print("wednesday")
elif h==4:
    print("thursday")
elif h==5:
    print("friday")
elif h==6:
    print("saturday")
else:
    print("sunday! rest")

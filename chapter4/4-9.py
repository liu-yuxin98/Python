
year=eval(input("enter a year"))

if(year%4==0 and year%100!=0):
    print("is leap year")
elif(year%400==0):
    print("is leap year")
else:
    print("isn't leap year")
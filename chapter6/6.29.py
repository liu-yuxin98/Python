#-*- coding=utf-8-*-
def doubleDigit(digit): # 每一位乘以二
    if digit >=5 :
        double = (2*digit) % 10 + 1
    else:
        double = 2*digit
    return double
def sumDoublednumber(number):
    sum=0
    count=0
    while number!=0:
        #print("number={}".format(number), end=" ")
        digit=number%10
        count+=1
        if count%2==0:
            sum += doubleDigit(digit)
        #print("digit={}".format(doubleDigit(digit)),end=" ")
        #print("sum={}".format(sum),end=" ")
        number = (number - number % 10) / 10
        print('\n')
    return sum
def sumOdd(number):
    count=0
    sum=0
    while number!=0:
        digit=number%10
        number=(number-number%10)/10
        count+=1
        if count%2==1:
            sum+=digit
    return sum
def isValid(number):
    if (sumDoublednumber(number)+sumOdd(number))%10==0:
        return 1
    else:
        return 0
print(sumDoublednumber(4388576018402626))

'''
number=eval(input("enter a card number:"))
print(sumDoublednumber(number))
print(sumOdd(number))
print(isValid(number))

'''


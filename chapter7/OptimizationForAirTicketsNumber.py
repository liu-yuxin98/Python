#-*-coding:utf-8-*-
from myOwnfunc import binomialDistribuation # 二项式分布计算概率
from myOwnfunc import  combination

'''
刘育鑫 写于2020.1.19
对应的问题是ted-ed中提出的。《为什么航空公司卖那么多机票》

'''

#计算预售numbersell个座位时，航空公司的预期收益
# p 是每一个乘客准点到达机场的概率

def calculateValue(numbersell,p):
    sum=numbersell*250
    for i in range(181,numbersell+1):  # 每一位买了票但是没有坐上飞机的需要退还800刀
        sum=sum-binomialDistribuation.binomialDistribuation(i,numbersell,p)*(i-180)*800
    return sum


def main():
    max=0
    index=181
    p=eval(input(" the arrival rate for each passenger is:"))
    for i in range(181,201): # calculate the except income for 181-200 seats
        print(i,end=" ")
        print(calculateValue(i,p))
        if calculateValue(i,p)>=max:
            max=calculateValue(i,p)
            index=i
    print("sell {} tickets earn higest money {}".format(index,max))

    
main()


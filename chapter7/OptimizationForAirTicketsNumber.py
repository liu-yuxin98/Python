#-*-coding:utf-8-*-
from myOwnfunc import binomialDistribuation # ����ʽ�ֲ��������
from myOwnfunc import  combination

'''
������ д��2020.1.19
��Ӧ��������ted-ed������ġ���Ϊʲô���չ�˾����ô���Ʊ��

'''

#����Ԥ��numbersell����λʱ�����չ�˾��Ԥ������
# p ��ÿһ���˿�׼�㵽������ĸ���

def calculateValue(numbersell,p):
    sum=numbersell*250
    for i in range(181,numbersell+1):  # ÿһλ����Ʊ����û�����Ϸɻ�����Ҫ�˻�800��
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


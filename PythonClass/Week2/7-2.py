# -*- coding: utf-8 -*-
# 2020-03-04
# author Liu,Yuxin

def isallNUmber(id): # check wether the 0-16 are all numbers
    num = ['1', '0', '9', '8', '7', '6', '5', '4', '3', '2']
    flag = 1
    for i in range(17):
        if id[i] not in num:  # not number
            flag = 0
    return flag

def getZ(s): # get z
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    result = [ i*0 for i in range(18)]
    for i in range(17):
        result[i] = eval(s[i])*weight[i]
    z = sum(result) % 11
    return z

def getM(z): # get m
    Mlist = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    return Mlist[z]

def check(id):  # check weather id is true or not
    id1 = id[:17]  # get 1-17
    if isallNUmber(id1) == 0:  # not all number
        return False
    else:
        z = getZ(id1)  # get z
        m = getM(z)  # get m
        if ord(m) == ord(id[-1]):  # check m
            return True
        else:
            return False

def FinalCheck(lis):  # check id list and output
    allpassed = 1
    for i in range(len(lis)):
        if check(lis[i]) == False:
            print(lis[i])
            allpassed = 0
    if allpassed == 1:
        print('All passed')


def main():
    n = eval(input())  # enter number
    slist = []
    for i in range(n):
        s = input()
        slist.append(s)

    FinalCheck(slist)

main()














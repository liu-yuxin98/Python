# -*- coding: utf-8 -*-
# 2020-03-11
# author Liu,Yuxin
'''
find the position of a word in a string
eg.
find 'is' inside 'this is a text is'
return [2,5,15]
'''
def findPosition(str,c):
    number = str.count(c)  # count how many times c appears in str
    if number == 0:
        return []
    else:
        index = str.find(c)
        lst =[index]
        for i in range(number-1):
            index = str.find(c, index+1, len(str))
            lst.append(index)
        return lst



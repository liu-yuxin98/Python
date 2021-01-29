# -*- coding: utf-8 -*-
# 2020-03-04
# author Liu,Yuxin
'''
def reverse(s):
    return s[::-1]

def sum(s):
    length = len(s)
    sum = 0
    for i in range(length):
        ti = ord(s[i])-ord('0')
        sum += ti
    return length,sum

def create(n):
    x = 0
    for i in range(n):
        x *= 10
        x += 6
    return x
'''

def isPalin(s):
    if s[::-1] == s:
        print(s)
        print('Yes')
    else:
        print(s)
        print('No')

s = input()
isPalin(s)

# -*- coding: utf-8 -*-
# 2020-03-02
# author Liu,Yuxin
def findstring(s1, s2):
    s3 = s2[::-1] # reverse s2
    index1 = s3.find(s1) # find the index of s1 inside s3
    if index1 == -1: # can't find s1 in s2
        print('Not Found')
    else:
        index = len(s2)-1-index1
        print('index = {}'.format(index))
s1 = input()
s2 = input()
findstring(s1, s2)


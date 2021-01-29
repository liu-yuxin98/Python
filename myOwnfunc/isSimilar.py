# -*- coding: utf-8 -*-
# 2020-02-07
# author Liu,Yuxin

def issimilar(s1,s2):
    lists1 = [ x for x in s1]
    lists2 = [x for x in s2]
    lists1.sort()
    lists2.sort()
    flag = 1
    for i in range(len(lists2)):
        if lists2[i] != lists1[i]:
            flag = 0
    return flag

print(issimilar('listen', 'silent'))


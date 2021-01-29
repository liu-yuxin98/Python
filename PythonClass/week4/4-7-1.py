# -*- coding: utf-8 -*-
# 2020-03-16
# author Liu,Yuxin
n = int(input())
if n == 0:
    print('average = '+str(0.0))
    print('count = ' + str(0))
else:
    gradelst = list(map(int, input().split()))
    avg = sum(gradelst) / n
    avg = round(avg, 1)
    count = len([k for k in gradelst if k >= 60])
    print('average = ' + str(avg))
    print('count = ' + str(count))



# -*- coding: utf-8 -*-
# 2020-03-10
# author Liu,Yuxin
s = input()
s = list(s)
if s[2]=='0' and s[1]=='0':
    s.pop(2)
    s.pop(1)
elif s[2]=='0' and s[1]!='0':
    s.pop(2)
s = s[::-1]
s = ''.join(s)
print(s)

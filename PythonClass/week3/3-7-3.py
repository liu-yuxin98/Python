# -*- coding: utf-8 -*-
# 2020-03-10
# author Liu,Yuxin
str = input().lstrip()
str = str.rstrip()
s1 = input().split()
news1 = ''.join(s1)
newstr = ''.join(str)
lst = [ t for t in newstr if t != news1.upper() and t != news1.lower()]
print('result: '+''.join(lst))


'''
if ord('a') <= ord(s1)<=ord('z'):
    s2 = chr(ord(s1)+ord('A')-ord('a'))
elif ord('A') <= ord(s1)<=ord('Z'):
    s2 = chr(ord(s1)+ord('a')-ord('A'))
'''


# print(str)
# print(s1, s2)

# print(newstr)


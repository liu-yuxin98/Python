# -*- coding: utf-8 -*-
# 2020-04-08
# author Liu,Yuxin

s = input().split(',')
num = int(input())
lst = [int(num) for num in s]

dic = {}
for i in range(len(s)):
    for j in range(i+1,len(s)):
        dic[lst[i]+lst[j]] = [i,j]

key = dic.keys()
if num in key:
    print(str(dic[num][0])+' '+str(dic[num][1]))
else:
    print('no answer')


'''

# 1
dic1 = eval(input().strip())
dic2 = eval(input().strip())
dic3 = dic1

for key in dic2.keys():
    if key in dic3:
        dic3[key] = dic3[key]+dic2[key]
    else:
        dic3[key] = dic2[key]
# print(dic3)

key3 = list(dic3.keys())
# print(key3)
# 记录字符串
dic3key = {key:0 for key in key3}
for key in key3:
    if type(key) == str:
        dic3key[key] = 1
# print(dic3key)

key3 = [ ord(key) if type(key)==str else key for key in key3]
key3.sort()

i = 0
while True:
    if chr(key3[i]) in dic3key:
        if i == len(key3)-1:
            if key3[i] == key3[i-1]:
                break
            else:
                key3[i] = chr(key3[i])
        elif key3[i] == key3[i+1]:
             key3[i] = chr(key3[i])
             i = i+1
        else:
            key3[i] = chr(key3[i])
    i = i+1
    if i >= len(key3):
        break
# print(key3)
dic4 = {}
for key in key3:
    dic4[key] = dic3[key]
print('{',end='')
key4 = list(dic4.keys())
value4 = list(dic4.values())
for i in range(0, len(dic4)):
    if i == len(dic4)-1:
        if type(key4[i])== str:
            print( '\"',end='')
            print(key4[i], end='')
            print('\"', end='')
            print(":", end='')
            print(value4[i], end='')
        else:
            print(key4[i],end='')
            print(":",end='')
            print(value4[i],end='')
    else:
        if type(key4[i]) == str:
            print('\"', end='')
            print(key4[i], end='')
            print('\"', end='')
            print(":", end='')
            print(value4[i], end='')
            print(',', end='')
        else:
            print(key4[i], end='')
            print(":", end='')
            print(value4[i], end='')
            print(',',end='')
print('}')
'''











'''
#4
a, b = map(int, input().split())
dic = {}
for num in range(a,b+1):
    if num%(3*5*7) == 0:
        dic[num] = 1
print(len(list(dic.keys())))

'''



'''
# 3
s = eval(input())
dic = {}
for num in s:
    dic[num] = dic.get(num, 0)+1
keys = list(dic.keys())
print(*keys)

'''




'''
# 2
x = eval(input())
z = input().strip()
y = eval(input())
result = {'+':'x+y','-':'x-y','*':'x*y','/':'x/y' if y!=0 else 'divided by zero'}
r = result[z]
if r =='divided by zero':
    print(r)
else:
    r = eval(r)
    print(format(r, '.2f'))
'''


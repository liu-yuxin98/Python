#coding:utf-8   # 出现中文的时候用
import turtle
print(format(57.89283091280,"5.2e")) #控制小数格式
print(format(8989.98090,"10.2%"))
print(format(7,"b"))
s=str(3.4)# convert number to string
t=str(2.6)
print(s+t) # 字符串加减
print(id(s),"  ", id(t))
print(" \"hello world \" ") #转义
print("aaa",end='')  #换行
print("bbb", end='')
print(ord('B')) #字符串的 ASC码
print(chr(98)) #ASC码对应字符
s="   WelcoMe  "
print(s.lower())
print(s.upper())
print(s.strip())  # 去除两边空格
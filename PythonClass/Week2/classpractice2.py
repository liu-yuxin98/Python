# -*- coding: utf-8 -*-
# 2020-03-02
# author Liu,Yuxin
'''
直播技术：视频->码流->阿里服务器->在发送到全国各地

作业回顾
1+1/3+1/5+...
需要找出通项，然后 sum[   ]

列表推导式

            字符串和列表元
————————————————————————————————————————————
字符串+元组+列表 -》序列容器
容器的基本特征： 容器本身的大小是动态可变的（比如茶杯其实是可以随着内部水的变化而变化）
python 容器可以分成两大类：1）序列容器 2）无序容器
序列容器：必须有下标（index)
两种方式操作：外部，内部
外部的：
x1+x2   /   x1*n  /     x[i]    /   len(x)  / min,max1  /


# 使用字符串表示身份证号码
"16010219805080118"
1980508
需要多切一片，到14（14开始不要了）

python 中非常重要的两点：列表推导式/切片

            字符串
————————————————————————————————
''' ''' as is
r raw 原封不动
字符串不可修改，不能修改字符串的内容


'''
print("hello"[1])  # "hello"的第二个
print([1,2,3,4,][0])  # [1,2,3,4]的第0号元素
print([1,2,3,4][-1])  # -1 是从右边数过来的最后一个 从右往左数 -1，-2，-3，-4 没有-5（out range)
print("16010219805080118"[6:14])  # [6:14] 实际取出的是6->13 在某个数字前切一刀
s = '32C' ; s1 = s[:-1] ; print(s1)  # 切片，从0开始，切刀最后一位为止, 0 可以省略
print('zhejiang'[3:100])    # 从第三号元素前面开始切，切到最后
print('zhejiang'[3:])  # 从第三号元素前面开始切，切到最后
s ='zhejiang'
print(s[::2])  # 0 2 4 6  step(步长）
print(s[3:0:-1]) # 步长是-1 划在数字的右边（与1相反）
print(s[::-1])  #取逆
print(s[::-1] == s )  # 判断回文
print(s[-1::-1]) # 可以全取逆序
a1 = [1,3,5,7]
a2 = a1  # 把a2 指向 a1的第0号元素
a2[0] = 4
a2 = a1[:]  # 此处a2与 a2无关， 赋值
#  ————————————————————————————————

s1 = 'hello\nworld'
print(s1)
s2 =r'hello\n world'
print(s2)
s = 'zhejiang university'
print(s.title()) # 实际是创造新的字符串
print(s)  # s 本身不可修改,不可以修改内部的字符
s = s.upper()  # 让s = s.title()
print(s)
print(s.find('Jiang'))  # 找不到，返回-1（不是最后一个）
print(s.replace('ZHEJIANG', 'SUZHOU'))
print(s)  # s依然不变
print('3//11//2018'.split('/'))  #会把字符串转化成列表
print(max((3,5,1,7,4)))
lst=[12, -5, -22, -10, -26, 35, 0, 49, 3, -21]
print(lst[100:])

# 切片
s = '627F'
print('s[:-2:-1] = ',end='')
# 第一步 第一个空中省略的是什么， 因为在-2前省略，且步长为-1，所以省略的是末尾
# 第二步 看切片的左右，因为步长-1， 所以切片在右
# 第三步 确定排序，因为步长-1 所以 从右往左
print(s[:-2:-1])
print("-----------")
print('s[-2::-1] =',end=' ')
# 第一步 第一个空中省略的是什么， 因为在-2后省略，且步长为-1，所以省略的是开头
# 第二步 看切片的左右，因为步长-1， 所以切片在右
# 第三步 确定排序，因为步长-1 所以 从右往左
print(s[-2::-1])
print("-----------")








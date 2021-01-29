# -*- coding: utf-8 -*-
# 2020-04-13
# author Liu,Yuxin

#四则运算使用字典 因为可扩展性，代码不经过改变也可以适应未来的变化


# 找画笔，使用字典，从中找出只存在一次的数

# 考试分数中的众数，使用字典，找到values中最大的
# 在c语言中需要自己构建一个字典


#列表两数字之和等于目标值，找出下标
'''
s = input().split()
lst = [int(num) for num in s]
taget = int(input())
hm = dict()
for i in range(len(lst)):
    if lst[i] in hm:
        print(hm[lst[i]],i)
        break
    hm[taget-lst[i]] = i
'''


# hash 算法,不用循环找到key，可以很快的找到key。计算的复杂度是C，优化代码.

# 判断空表  Not lst = True lst可以作为逻辑值
# 字符串前加 u，主要用于电脑不是以unicode作为字符集。
# books =[{"names":u"C#从入门到精通"}]

# 字典嵌套
'''
输入： END
学号，姓名
学号，课程，成绩
输出：学号，姓名，课程1，课程2，...,平均分

'''
# 使用的是数据结构
# studentid ,key=学号，value=姓名。
# score, key = 课程 ，value = 成绩
# studentscore， key = 学号 ，value = 字典
# 集合 course, 课程

# 实现过程
'''


'''
s = (46.5+70.8+34.5)/3
print(s)
'''
coursescore = {}

while True:
    line = input().strip()
    if line == 'END':
        break
    else:
        words = [x.strip() for x in line.split(',')]
        words[1] = float(words[1])
        coursescore[words[0]] = coursescore.get(words[0], [])
        coursescore[words[0]].append(words[1])

print(coursescore)
'''










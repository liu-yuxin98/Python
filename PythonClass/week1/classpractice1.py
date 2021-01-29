# -*- coding: utf-8 -*-
# 2020-03-02
# author Liu,Yuxin
'''
            分数构成
——————————————————————————————
     平时 30%
课内练习： 5%
每周一个实验：15%
每周一次作业：7.5%
期中考试：2.5%

    上机考试： 20%
至少对1题，

    期末理论 50%
卷面>55%
——————————————————————————————————
第一周（1,2章） 有MOOC，
优先级

2**2**3= 2**8=256

1   +- 单目（正负）
2   幂          从右向左
3   乘除
4   加减        从左向右
5   逻辑

'''
newlst = []
def flatten(lst):
    # flatten的作用（1）把一个List中（不论几层嵌套）都提取出来
    for x in lst:
        # 判断 x 能否被flatten
        if isinstance(x,(tuple,list)):
           flatten(x)
        else:
            # x 是字符串，需要被转化为 整数型的列表
            if type(x) == str:
                x = [int(i) for i in x]
                flatten(x)
            else:
                newlst.append(x)
lst = [1,2,3,[4,5,[7,8],9],'69',7]
flatten(lst)

print(__name__)







# -*- coding: utf-8 -*-
# 2020-04-13
# author Liu,Yuxin
tfile = open("score.txt", "rt")
copy = open("score_copy.txt", "w")
head = tfile.readline()
head = head[0:-1]
copy.write(head+str('   总分\n'))
lines = tfile.readlines()
l2 = []
for line in lines:
    line = line.split()
    print(line)
    sc = int(line[3])*0.5+int(line[4])*0.3+int(line[5])*0.2
    line.append(str(sc))
    print(line)
    line = '\t'.join(line)
    line = line+'\n'
    l2.append(line)

print(l2)
print(lines)
copy.writelines(l2)
copy.close()
tfile.close()


'''
source = open("cj.txt", "r")
back = open("cjback.txt","w")
s = source.read()
back.write(s)
source.close()
back.close()
# write into buffer, after close->buffer->txt
# readlines
f = open("score.txt","r")
head = f.readline()
print(head)
s = f.readlines()
print(s)
f.close()
# ANSI, UTF-8, GBK
# 打开编码为GBK的文件 open(filename,mode,encoding = "GBK")
# 词频统计,统计所有单词的个数以及词频最大的10%的单词
# 矩阵 matrix
lst = [[4,71,2,5],[58,114,94,2],[67,3,6,45]]
print(lst[2][1:3])
print(lst[1:3][1])
for row in lst:
    for column in row:
        print(column,end = '\t')
    print(' ')
# 矩阵转置 a[i][j] = i*n+j+1
# dataframe = excel


'''

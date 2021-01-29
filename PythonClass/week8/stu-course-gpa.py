# -*- coding: utf-8 -*-
# 2020-04-13
# author Liu,Yuxin
studentid ={}
studentscore = {}
course = set()
coursescore = {}
while True:
    line = input()
    if line == 'END':
        break
    words = [x.strip() for x in line.split(',')] # 去除两边空格
    if len(words) == 2:  # id,name
        studentid[words[0]] = words[1]
    else:  # id,course,grade
        # 为学生创建属于他的score的字典
        words[2] = float(words[2])
        score = studentscore.get(words[0], {})
        score[words[1]] = words[2]
        studentscore[words[0]] = score
        course.add(words[1])
        # 为计算每门课平均分做准备
        coursescore[words[1]] = coursescore.get(words[1], [])
        coursescore[words[1]].append(words[2])
# print head
print('student id, name, ', end='')
course = list(course)
course.sort()
for s in course:
    print(s, end=', ')
print('average')
# print each line
studentlst = list(studentid.keys())
studentlst.sort()

for i in range(len(studentlst)):
    print(studentlst[i], end=', ')
    print(studentid[studentlst[i]], end=', ')
    score = studentscore[studentlst[i]]
    avg = 0
    cnt = 0
    for j in range(len(course)):
        if course[j] in score:
            print(score[course[j]], end=', ')
            avg += score[course[j]]
            cnt += 1
        else:
            print('', end=', ')
    avg = round(avg/cnt, 1)
    print(avg)

print(', , ', end='')
# 计算每一门课的平均值
allavg = []
for i in range(len(course)):
    sumscore = sum(coursescore[course[i]])
    num = len(coursescore[course[i]])
    avg = sumscore/num
    allavg.append(avg)
    print(str(round(avg, 1)), end=', ')
allcourseavg = round(sum(allavg)/len(allavg), 1)
print(allcourseavg)












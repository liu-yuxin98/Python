# -*- coding: utf-8 -*-
# 2020-02-19
# author Liu,Yuxin
# check whether President.txt exists

'''
import os.path
if os.path.isfile('President.txt'):
    print("President.txt exists")
'''

outfile = open("President.txt","w")
outfile.write('Bill Clinton\n')
outfile.write("George Bush\n")
outfile.write('Barack Obama\n')
outfile.write('Donlord Trump')
outfile.close()
'''
infile = open("President.txt", "r")   # open file for input
print(infile.read())
infile.close()
print('------------------------')

# second method
infile = open("President.txt", "r")
s1 = infile.read(10)
print(s1)
infile.close()
print('------------------------')

# third method
infile = open("President.txt", "r")
line1 = infile.readline()
line2 = infile.readline()
print(line1)
print(line2)
infile.close()
print('------------------------')

# fourth method
infile = open("President.txt", "r")
z = infile.readlines()
print(infile.readlines())
infile.close()
print('------------------------')
'''

infile = open("President.txt", "r")
z = infile.readlines()
for i in range(4):
    print(z[i])





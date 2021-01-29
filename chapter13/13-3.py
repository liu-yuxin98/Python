# -*- coding: utf-8 -*-
# 2020-02-19
# author Liu,Yuxin
import os.path
import sys
def main():

    f2 = input('enter a file name:').strip()  # name f2
    # check if f2 exist
    if os.path.isfile(f2):
        print(f2+'exists')
        sys.exit()

    f1 = open(r"C:\P\homework\chapter13\President.txt", "r")  # open f1
    outfile = open(f2, "w")
    outlines = outchars = 0
    for line in f1:
        outlines += 1  # count line
        outchars += len(line)  # count chars
        outfile.write(line)   # write
    print('------------------')
    print(outlines, " lines and ")
    print(outchars, "chars")
    f1.close()
    outfile.close()


main()


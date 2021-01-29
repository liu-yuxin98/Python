# -*- coding: utf-8 -*-
# 2020-02-04
# author Liu,Yuxin
from tkinter import *
import math
class LoacCalculator:
    def __init__(self):
        # window and two frame
        window = Tk()
        window.title('Loan Calculator')

        # left 5 labels
        Label(window, text='Annual Interest Rate:').grid(row=1, column=1)
        Label(window, text='Number of years:').grid(row=2, column=1)
        Label(window, text='Loan Amount').grid(row=3, column=1)
        Label(window, text='Monthly payment').grid(row=4, column=1)
        Label(window, text='Total Payment').grid(row=5, column=1)
        # three Entry:
        self.AnnualIR = IntVar()
        self.NumberOY = IntVar()
        self.LoanA = IntVar()
        Entry(window, textvariable=self.AnnualIR).grid(row=1, column=2)
        Entry(window, textvariable=self.NumberOY).grid(row=2, column=2)
        Entry(window, textvariable=self.LoanA).grid(row=3, column=2)
        # two Label
        self.labelMp = Label(window, text=0)
        self.labelMp.grid(row=4, column=2)
        self.labelTp = Label(window, text=0)
        self.labelTp.grid(row=5, column=2)
        # one button
        Button(window, text='Calculate', command=self.Calculate).grid(row=6, column=2)

        window.mainloop()
    def Calculate(self):
        tp = self.LoanA.get()*math.pow((1+self.AnnualIR.get()/100), self.NumberOY.get())
        mp = tp/(12*self.NumberOY.get())
        self.labelMp['text'] = round(mp)
        self.labelTp['text'] = round(tp)

LoacCalculator()
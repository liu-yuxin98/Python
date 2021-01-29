# -*- coding: utf-8 -*-
# 2020-02-04
# author Liu,Yuxin
from tkinter import *
class ChangeLabelcolor():
    def __init__(self):
        window = Tk()
        window.title('Change label color')
        # add a label to frame1
        frame1 = Frame(window)
        frame1.pack()
        self.lbl = Label(frame1, text='', bg='green', fg='white')
        self.lbl.pack()

        # add a label to frame2
        frame2 = Frame(window)
        frame2.pack()
        label2 = Label(frame2, text='enter text')

        # add a entery
        self.msg = StringVar()
        entry = Entry(frame2, textvariable=self.msg)

        # add a button(to change text)
        btChange = Button(frame2, text='change text', command=self.changeText)
        # grid entry, label2,btChange
        label2.grid(row=1, column=1)
        entry.grid(row=1, column=2)
        btChange.grid(row=1, column=3)

        # add frame3 and
        frame3 = Frame(window)
        frame3.pack()

        '''
        # add two Button to change color
        btRed = Button(frame3, text='Red', bg='red', fg='white', command=self.toRed)
        btBlack = Button(frame3, text='Black', bg='black', fg='white', command=self.toBlack)
        btRed.grid(row=1, column=1)
        btBlack.grid(row=1, column=2)
        '''
        # add to radioButton
        self.var = StringVar()
        rbRed=Radiobutton(frame3, variable=self.var, value='R', text='Red', bg='red',
                          command=self.changecolor)
        rbYellow=Radiobutton(frame3, variable=self.var, value='Y', text='Yellow', bg='yellow',
                             command=self.changecolor)
        rbRed.grid(row=1, column=1)
        rbYellow.grid(row=1, column=2)




        window.mainloop()

        # write def for btChange
    def changeText(self):
        self.lbl['text'] = self.msg.get() # new text for lbl, from entry
    # change lbl['fg'] to red
    def toRed(self):
        self.lbl['fg'] = 'red'

    # change lbl['fg'] to black
    def toBlack(self):
        self.lbl['fg'] = 'black'
    # def for radiobutton
    def changecolor(self):
        if self.var.get() == 'R':
            self.lbl['fg'] = 'red'
        elif self.var.get() == 'Y':
            self.lbl['fg'] = 'yellow'


ChangeLabelcolor()










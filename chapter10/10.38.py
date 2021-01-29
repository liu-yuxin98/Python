# -*- coding: utf-8 -*-
# 2020-02-07
# author Liu,Yuxin

from tkinter import *
import random
window=Tk()
window.title('my window')
window.geometry('600x600')
canvas = Canvas(window, width=500, height=500)
canvas.pack()
listx1 = []
x1 = 50 # start from50
y2 = 300
listy1 = []
for i in range(10):
    y1 = random.randint(150, 250)
    listy1.append(y1)
    listx1.append(x1)
    x1 += 30 # width

for i in range(10):
    canvas.create_rectangle(listx1[i], listy1[i], listx1[i]+30, y2, tags='Rectangle')

def shuffle():
    canvas.delete('Rectangle')
    random.shuffle(listy1)
    for i in range(10):
        canvas.create_rectangle(listx1[i], listy1[i], listx1[i] + 30, y2, tags='Rectangle')
        if i == 9 :
            canvas.create_rectangle(listx1[i], listy1[i], listx1[i] + 30, y2, fill= 'blue', tags='Rectangle')


sbutton = Button(window, text='shuffle', command= shuffle)
sbutton.pack()
window.mainloop()



'''
class Rectangle:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
def shuffle():
    random.shuffle(Rectanglelist)
    canvas.delete('Rectangle')
    for i in range(5):
        canvas.create_rectangle(Rectanglelist[i].x1, Rectanglelist[i].y1,
                                Rectanglelist[i].x2, Rectanglelist[i].y2, tags='Rectangle')

Rectanglelist=[]
x1 = 100
x2 = x1+30
for i in range(5):
    z = random.randint(0, 100)
    y1 = 150+z
    y2 = 300
    r = Rectangle(x1, y1, x2, y2)
    Rectanglelist.append(r)
    x1 += 30
    x2 += 30

for i in range(5):
    canvas.create_rectangle(Rectanglelist[i].x1, Rectanglelist[i].y1,
                            Rectanglelist[i].x2, Rectanglelist[i].y2 )

shuffleButton =Button(window, text='shuffle', command=shuffle())
shuffleButton.pack()

'''




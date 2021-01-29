# -*- coding: utf-8 -*-
# 2020-02-01
# author Liu,Yuxin
from tkinter import *
import random
window=Tk()
window.title('扑克牌洗牌游戏')
window.geometry('800x600')

labellist=[]
imagelist=[]
for i in range(1,8):
    imagelist.append(PhotoImage(file=str(i)+'.gif')) # 可以创建图片列表

for i in range(3):
    labellist.append(Label(window,text='love you', font=('arial',15), image=imagelist[i]))
    labellist[i].grid(row=1,column=i)

def shuffle():
    random.shuffle(imagelist)
    for i in range(3):
        labellist[i]['image']=imagelist[i]



shuffleB = Button(window,text='Shuffle',font=('Arial',15),command=shuffle)
shuffleB.grid(row=2,column=2)
window.mainloop()




'''
var1=StringVar()
#var2=StringVar()
#var3=StringVar()
label1=Label(window,textvariable=var1,font=('Arial',12))

cardList=[ x for x in range(53)]
kinds=['梅花','方片','红桃','黑桃']
ranks=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
canvas=Canvas(window,bg='green',height=400,width=300)
#cardList[1]
imagelist=[]
for i in range(1,4):
    imagelist.append(PhotoImage(file=str(i)+'.gif'))

labellist=[]
for i in range(4):
    labellist.append(Label(window, image=imagelist[random.randint(1, 3)]))
    labellist[i].pack(side=LEFT)

'''


'''
def get_Poke():
    random.shuffle(cardList)
    kind = kinds[cardList[1] // 13]
    rank = ranks[cardList[1] % 13]
    var1.set(kind+rank)
    imagefile=imagelist[random.randint(0,2)]
    image = canvas.create_image(0, 0, anchor='n', image=imagefile)



shuffleButton = Button(window,text='Shuffle',font=('Arial',15),command=get_Poke)
#label1.grid(row=1, column=1)
#shuffleButton.grid(row=2, column=1)
#canvas.grid(row=1,column=2)

'''


window.mainloop()



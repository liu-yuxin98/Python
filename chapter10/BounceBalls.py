# -*- coding: utf-8 -*-
# 2020-02-04
# author Liu,Yuxin
'''
            Ball
—————————————————————————
x:int
y:int
dx:int
dy:int
color: str
radius:int
_________________________
Ball(x,y,dx,dy,color,radius)
setx start from (0,0)
sety
setdx   (2)
setdy   (2)
setcolor( get random color)
setradius ( 1-5)
____________________________________
****************************************
________________________________________
            BounceBall
window
canvas
balllist
addbutton
stopbutton
restartbutton
speedupbutton
speeddownbutton
_________________________________________
stop
restart
add
remove

'''




from tkinter import *
import random
import math

# get a radndom color from #RRGGBB
def getRandomcolor():
    HexList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    color = '#'
    for i in range(6):
        color = color + HexList[random.randint(0, 15)]
    return color
class Ball:
    def __init__(self, x, y, dx, dy, color, radius):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color
        self.radius = radius

class BounceBall:
    def __init__(self):
        window = Tk()
        window.title('Bounce Ball')
        # draw canvas
        self.width = 300
        self.height = 200
        self.canvas = Canvas(window, bg='white', width=self.width, height=self.height)
        self.canvas.pack()
        # create a ball list
        self.balllist = []
        # create add button
        addButton = Button(window, text='add bounce ball', command=self.add)
        addButton.pack()
        # create speed up button
        speedupButton = Button(window, text='speed up', command=self.speedup)
        speedupButton.pack()
        # create speed down button
        speeddownButton = Button(window, text='speed down', command=self.speeddown)
        speeddownButton.pack()
        # stop
        stopButton = Button(window, text='stop', command=self.stop)
        stopButton.pack()
        # remove the last ball
        removeButton = Button(window, text='remove', command=self.remove)
        removeButton.pack()
        # restart
        restartButton = Button(window, text='restart', command=self.restart)
        restartButton.pack()


        self.isStop = False
        self.sleepTime = 100
        self.animate()
        window.mainloop()

    # restart
    def restart(self):
        self.isStop = False
        self.animate()
    # remove
    def remove(self):
        self.balllist.pop()
    # stop
    def stop(self):
        self.isStop = True


    # speed up
    def speedup(self):
        for ball in self.balllist:
            ball.dx = ball.dx + 1
            ball.dy = ball.dy + 1


    # speed down
    def speeddown(self):
        for ball in self.balllist:
            ball.dx = ball.dx + 1
            ball.dy = ball.dy + 1





    # add a new ball
    def add(self):
        # set move direction
        flag = random.randint(0, 1)
        if flag == 0:
            dx = 2
        else:
            dx = -2
        # set dy
        dy = 4*random.random()

        color = getRandomcolor() # set color
        radius = random.randint(5,15)  # set radius [2,5]
        x = self.width/2  # set start place
        y = radius # set start place
        self.balllist.append(Ball(x, y, dx, dy, color, radius))

    # animate ball movement
    def animate(self):
        while not self.isStop:
            self.canvas.after(self.sleepTime)
            self.canvas.update()
            self.canvas.delete('ball')
            for ball in self.balllist:
                self.redisplayBall(ball)

    def redisplayBall(self, ball):
        listx1 = []  # 记录在x方向发生碰撞的两个球 ，这是球1
        listx2 = []  # 记录在x方向发生碰撞的两个球 ，这是球2
        bounce = False
        # 判断在balllist中有几个球相撞
        number = len(self.balllist)
        for i in range(number):
            for j in range(i , number):
                y = math.fabs(self.balllist[i].y - self.balllist[j].y)
                x = math.fabs(self.balllist[i].x - self.balllist[j].x)
                z = math.fabs(self.balllist[i].radius + self.balllist[j].radius)
                if math.pow(x, 2)+math.pow(y, 2) <= math.pow(z,2):
                    bounce = True
                    listx1.append(i)
                    listx2.append(j)

        if bounce == True:
            lenx = len(listx1)
            # 改变 x 方向碰撞的球
            for i in range(lenx):
                self.balllist[listx1[i]].dx = -self.balllist[listx1[i]].dx  # 第一个球改变 dx
                self.balllist[listx1[i]].dy = -self.balllist[listx1[i]].dy  # 第一个球改变 dy
                self.balllist[listx2[i]].dx = -self.balllist[listx2[i]].dx  # 第二个球改变 dx
                self.balllist[listx2[i]].dy = -self.balllist[listx2[i]].dy  # 第二个球改变 dy
        if ball.x > (self.width - ball.radius) or ball.x < ball.radius:  # 到达左右两边
            ball.dx = -ball.dx
        if ball.y > (self.height - ball.radius) or ball.y < ball.radius:  # 到达上下两边
            ball.dy = -ball.dy


        ball.x += ball.dx  # move dx
        ball.y += ball.dy  # move dy
        self.canvas.create_oval(ball.x-ball.radius, ball.y-ball.radius,
                                ball.x+ball.radius, ball.y+ball.radius,
                                fill=ball.color, tags='ball')


BounceBall() # create GUI












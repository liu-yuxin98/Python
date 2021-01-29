from tkinter import *
'''
window=Tk() # create window
window.title('My window') # name window
window.geometry('300x300') # width*length
l=Label(window,textvariable='MOG! this is TK',bg="gray",width=15,height=2) # attribute of label
# txt-> 文本 bg->background color font->字体
#l.place(height=100,width=200) #label右下角的坐标
l.pack() # place
window.mainloop() # main loop'''
def processOK():
    print("OK button is clicked")
def processCancel():
    print("cancel button is clicked")
window=Tk()
btOk=Button(window,text="ok",fg="red",command=processOK())
btcancel=Button(window,text="cancel",bg="yellow",command=processCancel())
btOk.pack()
btcancel.pack()
window.mainloop()





'''
label=Label(window,text="welcom to Python")
button=Button(window,text="click")
label.pack()
button.pack()
window.mainloop()
'''

from tkinter import *
class WidgetsDemo:
    def __init__(self):
        window=Tk()
        window.title("Widgets Demo")
        window.geometry("300x300")

        # add a check button , a radio button to frame1
        frame1=Frame(window)# create a frame to window
        frame1.pack()
        self.v1 = IntVar()
        cbtBold=Checkbutton(frame1,text="Bold",variable=self.v1,
                            command=self.processCheckbutton())
        self.v2=IntVar()
        rbRed = Radiobutton(frame1,text="red", bg="red", variable=self.v2, value=1,\
                          command=self.processRadiobutton())
        ybyellow = Radiobutton(frame1, text="yellow", bg="yellow",variable=self.v2,\
                             value=2, command=self.processRadiobutton())
        cbtBold.grid(row=1,column=1)
        rbRed.grid(row=1,column=2)
        ybyellow.grid(row=1,column=3)

        # add a label, an entry, a button and a message to frame2
        frame2 = Frame(window)# create and add a frame to window
        frame2.pack()
        label = Label(frame2, text="enter your name:")
        # entry
        self.name = StringVar()
        entryName = Entry(frame2, textvariable=self.name)
        # button
        btGetName = Button(frame2, text="Get Name", command=self.processButton())
        #message
        message = Message(frame2, text="It is a widgets demo")
        label.grid(row=2, column=1)
        entryName.grid(row=2,column=2)
        btGetName.grid(row=3,column=1)
        message.grid(row=3,column=2)

        #add text
        text=Text(window)
        text.pack()
        text.insert(END,
                    "The best way to learn is to read")
        text.insert(END,
                    "use the examples to learn")
        text.insert(END,
                    "creat your own application")

        window.mainloop()

    def processCheckbutton(self):
        print("check button is")
        if self.v1.get() == 1:
            print("Checked")
        else:
            print("Unchecked")

    def processRadiobutton(self):
        if self.v2.get()==1:
            print("Red",end=" ")
        else:
            print("Yellow",end=" ")
        print("is selected")

    def processButton(self):
        print("your name is"+self.name.get())



w1=WidgetsDemo()
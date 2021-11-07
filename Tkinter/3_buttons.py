from tkinter import *


root = Tk()


def myClick():
    myLabel = Label(root, text='Look!, I cliked a button!')
    myLabel.pack()

# buttons are also widgets
myButtom = Button(root, text="Click Me!", padx=50, pady=50, command=myClick) # the function is called without parenthesis
myButtom.pack()

root.mainloop()

from tkinter import *


root = Tk()

# create entry widget
e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name: ")

def myClick():
    hello = "Hello, " + e.get() + "!"
    myLabel = Label(root, text=hello) # shows in the widget the entered text
    myLabel.pack()

# buttons are also widgets
myButtom = Button(root, text="Enter your name: ", padx=50, pady=50, command=myClick) # the function is called without parenthesis
myButtom.pack()

root.mainloop()

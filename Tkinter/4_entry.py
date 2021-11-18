import tkinter

root = tkinter.Tk()

# create entry widget
e = tkinter.Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name: ")


def myClick():
    hello = "Hello, " + e.get() + "!"
    myLabel = tkinter.Label(root,
                            text=hello)  # shows in the widget the entered text
    myLabel.pack()


# buttons are also widgets
# the function is called without parenthesis
myButtom = tkinter.Button(root,
                          text="Name: ", padx=50, pady=50, command=myClick)
myButtom.pack()


root.mainloop()

import tkinter


root = tkinter.Tk()


def myClick():
    myLabel = tkinter.Label(root, text='Look!, I cliked a button!')
    myLabel.pack()


# buttons are also widgets
# the function is called without parenthesis
myButtom = tkinter.Button(root,
                          text="Click Me!", padx=50, pady=50, command=myClick)

myButtom.pack()

root.mainloop()

from tkinter import Button, Label, Scale, Tk, mainloop
from tkinter.constants import HORIZONTAL

root = Tk()
root.geometry("400x400")


# function to update the value and resize window
def slide():
    global my_label
    root.geometry(str(horizontal.get()) + "x" +
                  str(vertical.get()))  # resize the window


vertical = Scale(root, from_=0, to=400)  # create vertical slider
vertical.pack()

# create horizontal slider
horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()


my_btn = Button(root, text="Click Me!", command=slide).pack_configure()


root.mainloop()

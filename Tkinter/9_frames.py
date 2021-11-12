from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Learn to code')

# create frame
my_frame = LabelFrame(root, padx=50, pady=50)
my_frame.pack(padx=10, pady=10)

# add two buttons to the frame
b = Button(my_frame, text="Don't click here!")
b2 = Button(my_frame, text="Click here!")
# put buttons onto the screen in a grid
b.grid(row=0, column=0)
b2.grid(row=1, column=1)


root.mainloop()

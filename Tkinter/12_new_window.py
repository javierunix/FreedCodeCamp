import os
from tkinter import Button, Label, Tk, Toplevel, mainloop
from PIL import ImageTk, Image


dirname = os.path.dirname(__file__)
image_path = os.path.join(dirname, 'img_gallery/img_1.jpg')

# create root window
root = Tk()
root.title("Learn to Code!")


def open_window():
    global my_img
    top = Toplevel()
    top.title("Floating ballon!")
    my_img = ImageTk.PhotoImage(Image.open(image_path))  # load image
    my_label = Label(top, image=my_img)
    my_label.pack()
    btn2 = Button(top, text="Close window", command=top.destroy).pack()


btn = Button(root, text="Open second window", command=open_window).pack()


mainloop()

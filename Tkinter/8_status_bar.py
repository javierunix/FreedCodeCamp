import os
from tkinter import Tk, Label, Button, W, E
from tkinter.constants import SUNKEN
from PIL import ImageTk, Image


dirname = os.path.dirname(__file__)


root = Tk()
root.title("Learn to Code at Codemy.com")

icon_path = os.path.join(dirname, 'icons/icon2.ico')

image_path1 = os.path.join(dirname, 'img_gallery/img_1.jpg')
image_path2 = os.path.join(dirname, 'img_gallery/img_2.jpg')
image_path3 = os.path.join(dirname, 'img_gallery/img_3.jpg')
image_path4 = os.path.join(dirname, 'img_gallery/img_4.jpg')
image_path5 = os.path.join(dirname, 'img_gallery/img_5.jpg')


root.iconbitmap(icon_path)

my_image_1 = ImageTk.PhotoImage(Image.open(image_path1))
my_image_2 = ImageTk.PhotoImage(Image.open(image_path2))
my_image_3 = ImageTk.PhotoImage(Image.open(image_path3))
my_image_4 = ImageTk.PhotoImage(Image.open(image_path4))
my_image_5 = ImageTk.PhotoImage(Image.open(image_path5))

my_image_list = [my_image_1, my_image_2, my_image_3, my_image_4, my_image_5]

image_index = 0  # index of the first image

# status bar
my_text = "Image %s of %s" % (str(image_index + 1), str(len(my_image_list)))
status = Label(root, text=my_text, bd=1, relief=SUNKEN, anchor=E)
# bd = border, E= east (rigth), w= west (left)

# show the first image
my_label = Label(image=my_image_list[image_index])
my_label.grid(row=0, column=0, columnspan=3)


def forward():
    global my_label
    global image_index
    my_label.grid_forget()  # get rid of the current image
    image_index += 1  # increase the index of the picture
    # using the module operator, when the beginning of the list is reached
    # we start again
    image_index = image_index % len(my_image_list)
    my_label = Label(image=my_image_list[image_index])
    my_label.grid(row=0, column=0, columnspan=3)
    # update the status bar
    my_text = "Image %s of %s" % (
        str(image_index + 1), str(len(my_image_list)))
    status = Label(root, text=my_text, bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back():
    global my_label
    global image_index
    my_label.grid_forget()  # get rid of the current image
    image_index -= 1  # decrease the index of the picture
    # using the module operator, when the beginning of the list is reached
    # we start again
    image_index = image_index % len(my_image_list)
    my_label = Label(image=my_image_list[image_index])
    my_label.grid(row=0, column=0, columnspan=3)
    # update the status bar
    my_text = "Image %s of %s" % (
        str(image_index + 1), str(len(my_image_list)))
    status = Label(root, text=my_text, bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


# create buttons
button_back = Button(root, text="<<", command=back)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=forward)

# put buttons onto the screen
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)

# put the status bar onto the screen
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()

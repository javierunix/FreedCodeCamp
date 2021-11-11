from tkinter import Tk, Label, Button
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to Code at Codemy.com")

icon_path = '/Users/xabier/Documents/FreeCodeCamp/Tkinter/icons/icon2.ico'
image_path = '/Users/xabier/Documents/FreeCodeCamp/Tkinter/img_gallery/'


root.iconbitmap(icon_path)

my_image_1 = ImageTk.PhotoImage(Image.open(image_path + 'img_1.jpg'))
my_image_2 = ImageTk.PhotoImage(Image.open(image_path + 'img_2.jpg'))
my_image_3 = ImageTk.PhotoImage(Image.open(image_path + 'img_3.jpg'))
my_image_4 = ImageTk.PhotoImage(Image.open(image_path + 'img_4.jpg'))
my_image_5 = ImageTk.PhotoImage(Image.open(image_path + 'img_5.jpg'))

my_image_list = [my_image_1, my_image_2, my_image_3, my_image_4, my_image_5]

image_index = 0  # index of the first image

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
    my_label = Label(image=my_image_list[image_index % len(my_image_list)])
    my_label.grid(row=0, column=0, columnspan=3)


def back():
    global my_label
    global image_index
    my_label.grid_forget()  # get rid of the current image
    image_index -= 1  # decrease the index of the picture
    # using the module operator, when the beginning of the list is reached
    # we start again
    my_label = Label(image=my_image_list[image_index % len(my_image_list)])
    my_label.grid(row=0, column=0, columnspan=3)


# create buttons
button_back = Button(root, text="<<", command=back)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=forward)

# put buttons onto the screen
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()

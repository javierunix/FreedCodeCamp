import os
from tkinter import Button, Label, Tk, mainloop, filedialog
from PIL import ImageTk, Image


dirname = os.path.dirname(__file__)
image_path = os.path.join(dirname, 'img_gallery/img_1.jpg')

# create root window
root = Tk()
root.title("Learn to Code!")


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir=os.path.join(dirname, 'img_gallery'),
                                               title="Select a file", filetypes=(("jpg files", "*.jpg"),
                                                                                 ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_label_label = Label(image=my_image).pack()


my_btn = Button(root, text="Open file", command=open).pack()

mainloop()

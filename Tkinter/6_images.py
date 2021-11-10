from tkinter import *
from PIL import ImageTk, Image # for managing usual images files (jpg, png,...)

root = Tk()
root.title("Learn to Code at Codemy.com")
root.iconbitmap('/Users/xabier/Documents/FreeCodeCamp/Tkinter/icons/trash_bin_recycle_bin_waste_dumpster_icon_191911.ico')

my_image = ImageTk.PhotoImage(Image.open('/Users/xabier/Documents/FreeCodeCamp/Tkinter/images/dices.png'))
my_label = Label(image=my_image)
my_label.pack()


button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()


root.mainloop()

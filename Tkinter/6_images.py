import tkinter
from PIL import ImageTk, Image

root = tkinter.Tk()
root.title("Learn to Code at Codemy.com")

icon_path = '/Users/xabier/Documents/FreeCodeCamp/Tkinter/icons/icon2.ico'
image_path = '/Users/xabier/Documents/FreeCodeCamp/Tkinter/images/dices.png'

root.iconbitmap(icon_path)

my_image = ImageTk.PhotoImage(Image.open(image_path))
my_label = tkinter.Label(image=my_image)
my_label.pack()


button_quit = tkinter.Button(root, text="Exit Program", command=root.quit)
button_quit.pack()


root.mainloop()

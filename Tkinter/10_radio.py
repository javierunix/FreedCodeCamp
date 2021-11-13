from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Learn to code')

# tinker variable for the radio-button
# r = IntVar()  # tinker int variable
# r.set(2)

toppings = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("York", "York")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in toppings:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)


def clicked(value):
    my_label = Label(root, text=value)
    my_label.pack()


"""
# create radio-buttons
Radiobutton(root, text='Option 1', variable=r, value=1,
            command=lambda: clicked(r.get())).pack()
Radiobutton(root, text='Option 2', variable=r, value=2,
            command=lambda: clicked(r.get())).pack()
my_label = Label(root, text=pizza.get())
my_label.pack()
"""

my_button = Button(root, text='Click Me!',
                   command=lambda: clicked(pizza.get()))
my_button.pack()


root.mainloop()

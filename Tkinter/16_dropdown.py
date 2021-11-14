from tkinter import Button, Label, OptionMenu, StringVar, Tk


root = Tk()
root.geometry("400x400")


def show_value():
    my_label = Label(root, text=my_string_var.get())
    my_label.pack()


# define the list of options
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

# drop down boxes
my_string_var = StringVar()  # define the dropdown variable
my_string_var.set(options[0])  # set the default value
drop = OptionMenu(root, my_string_var, *options)
drop.pack()

my_button = Button(root, text="Show Selection", command=show_value).pack()


root.mainloop()

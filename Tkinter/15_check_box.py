from tkinter import Button, Checkbutton, IntVar, Label, StringVar, Tk


root = Tk()
root.geometry("400x400")


def show_value():
    my_label = Label(root, text=my_var.get())
    my_label.pack()


# create a tkinter integer variable
my_var = StringVar()

# create checkbox
my_check_box = Checkbutton(root, text="Check Me!",
                           variable=my_var, onvalue="On", offvalue="Off")
my_check_box.pack()

my_button = Button(root, text="Show Selection", command=show_value).pack()


root.mainloop()

from tkinter import Button, Label, Tk, mainloop, messagebox

root = Tk()
root.title("Learn to Code!")


def popup():
    response = messagebox.askyesno(title="This is my popup!",
                                   message="Hello, World!")
    if response == 1:
        Label(root, text="You clicked yes!").pack()
    else:
        Label(root, text="You clicked no!").pack()


Button(root, text='Pop Up!', command=popup).pack()


mainloop()

import tkinter


# In tkinter everything is a widget.
# 1. Create is the root widget
root = tkinter.Tk()

# 2. Create label widget.
myLabel1 = tkinter.Label(root, text="Hello, World!")
myLabel2 = tkinter.Label(root, text="My Name is Xabier Guijarro")

# 3. Put the label into the root.
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)


# 4. Create and envent loop
root.mainloop()

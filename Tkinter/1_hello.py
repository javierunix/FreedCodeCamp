import tkinter


# In tkinter everything is a widget.
# 1. Create is the root widget
root = tkinter.Tk()

# 2. Create label widget.
myLabel = tkinter.Label(root, text="Hello, World!")

# 3. Put the label into the root.
myLabel.pack()

# 4. Create and envent loop
root.mainloop()

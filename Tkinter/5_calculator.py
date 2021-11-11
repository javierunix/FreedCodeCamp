import tkinter

root = tkinter.Tk()
root.title("Simple Calculator")

# create entry widget
e = tkinter.Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# buttom_click add a new digit to the cell
def button_click(number):
    current = e.get()  # save the current value
    e.delete(0, tkinter.END)  # delete the content
    e.insert(0, str(current) + str(number))


# buttom_clear delete the content of the cell
def button_clear():
    e.delete(0, tkinter.END)


def button_add():
    first_number = e.get()  # get the content of the cell
    global f_num  # create a global variable
    global math
    math = "adition"
    f_num = int(first_number)  # save in the global variable as integer
    e.delete(0, tkinter.END)


def button_substract():
    first_number = e.get()  # get the content of the cell
    global f_num  # create a global variable
    global math
    math = "substraction"
    f_num = int(first_number)  # save in the global variable as integer
    e.delete(0, tkinter.END)


def button_multiply():
    first_number = e.get()  # get the content of the cell
    global f_num  # create a global variable
    global math
    math = "multiplication"
    f_num = int(first_number)  # save in the global variable as integer
    e.delete(0, tkinter.ENDND)


def button_divide():
    first_number = e.get()  # get the content of the cell
    global f_num  # create a global variable
    global math
    math = "division"
    f_num = int(first_number)  # save in the global variable as integer
    e.delete(0, tkinter.END)


def button_equal():
    second_number = e.get()  # save the content in a variable
    e.delete(0, tkinter.END)  # delete cell content

    if math == "adition":
        e.insert(0, f_num + int(second_number))

    elif math == "substraction":
        e.insert(0, f_num - int(second_number))

    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))

    elif math == "division":
        e.insert(0, f_num / int(second_number))


# to pass and argument in the command we have to use lambda
button_1 = tkinter.Button(root,
                          text="1", padx=40, pady=20,
                          command=lambda: button_click(1))
button_2 = tkinter.Button(root,
                          text="2", padx=40, pady=20,
                          command=lambda: button_click(2))
button_3 = tkinter.Button(root,
                          text="3", padx=40, pady=20,
                          command=lambda: button_click(3))
button_4 = tkinter.Button(root,
                          text="4", padx=40, pady=20,
                          command=lambda: button_click(4))
button_5 = tkinter.Button(root,
                          text="5", padx=40, pady=20,
                          command=lambda: button_click(5))
button_6 = tkinter.Button(root,
                          text="6", padx=40, pady=20,
                          command=lambda: button_click(6))
button_7 = tkinter.Button(root,
                          text="7", padx=40, pady=20,
                          command=lambda: button_click(7))
button_8 = tkinter.Button(root,
                          text="8", padx=40, pady=20,
                          command=lambda: button_click(8))
button_9 = tkinter.Button(root,
                          text="9", padx=40, pady=20,
                          command=lambda: button_click(9))
button_0 = tkinter.Button(root,
                          text="0", padx=40, pady=20,
                          command=lambda: button_click(0))
button_equal = tkinter.Button(root,
                              text="=", padx=91, pady=20,
                              command=button_equal)

# for button_clear there is no need of lambda, because no argument is passed
button_clear = tkinter.Button(root,
                              text="Clear", padx=79, pady=20,
                              command=button_clear)

button_add = tkinter.Button(root, text="+", padx=39,
                            pady=20, command=button_add)
button_substract = tkinter.Button(root, text="-", padx=40,
                                  pady=20, command=button_substract)
button_multiply = tkinter.Button(root, text="*", padx=40,
                                 pady=20, command=button_multiply)
button_divide = tkinter.Button(root, text="/", padx=40,
                               pady=20, command=button_divide)

# put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_substract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)


root.mainloop()

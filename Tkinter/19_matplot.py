import numpy as np
import matplotlib.pyplot as plt

from tkinter import Button, Tk

root = Tk()
root.title("Codemy.com - Learn to Code!")
root.geometry("400x200")


def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.polar(house_prices)
    plt.show()


myButton = Button(root, text="Graph it!", command=graph)
myButton.pack()


root.mainloop()

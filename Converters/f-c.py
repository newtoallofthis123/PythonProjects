import math
from tkinter import *


gui = Tk()
gui.configure(bg="black")
gui.geometry("600x600")
gui.title("Temperature Converter")
#gui.resizable(False,False)

def fc():
    farhenhiet = (f.get())
    farh = float(farhenhiet)
    celcius = float(farh-32)
    cel = 5/9 * celcius
    cel = str.c.get()

f = StringVar()
c = StringVar()
menu = StringVar

label = Label(
    gui,
    bg="black",
    fg="white",
    text="Farenhiet to Celcius Convertor",
    font=("Cascadia Code", 24)
    ).pack()

menu = Menu(gui).pack()
menu.add_command(label="F to C", command=fc)






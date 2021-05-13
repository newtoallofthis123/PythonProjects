# Name of the Project : clock.py
# Written by NoobScience : https://github.com/newtoallofthis123
# Modules Used : tkinter, time

''' The following is registered under the MIT License, NoobScience 2021. You are free to use it
as you like as long as you know what you are doing.
Enjoy using and check some of my other projects at https://github.com/newtoallofthis123'''

# Don't Change the code after this line unless you know what you are doing.

#! /usr/bin/env python3

'''
A simple clock widget for your laptop. Available for Windows, Mac and Linux
Written in Python '''

# Importing the necessary Modules
from tkinter import *
from tkinter.ttk import *

from time import strftime

# Making the tkinter gui
gui = Tk()

gui.title('Digital clock Widget by NoobScience')
gui.configure(bg='#002240')
gui.resizable(False,False)
photo = PhotoImage(file = "/clock.png")
gui.iconphoto(False, photo)

# Defining a new function clocktime to be used:
def clocktime():
	tick = strftime('%H:%M:%S %p')

	label.config(text =tick)

	label.after(1000, clocktime)

# Creating the anchor to hold our function clocktime:
label = Label(gui, font =('sans', 80), background = '#002240', foreground = '#FFC900')
label.pack(anchor= 'center')

#Calling our function
clocktime()
mainloop()

# Enjoy

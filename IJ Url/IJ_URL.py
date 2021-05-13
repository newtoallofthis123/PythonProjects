# Name of the Project : IJ-URL.py
# Written by NoobScience : https://github.com/newtoallofthis123
# Modules Used : pyperclip, pyshorteners, tkinter
#Installation of modules: pip install pyperclip, pip install pyshorteners

# Don't Change the code after this line unless you know what you are doing.

#! /usr/bin/env python3

'''
A simple program written in python, It uses git.io to shorten the url, git.io is the shortner by github. By NoobScience. To use it,
just switch to the directory you stored it in and open the terminal there and
type "python IJ_URL.py"
Available for Windows, Mac, Linux and written in python'''

# Import the Necessary Modules
import pyperclip
import pyshorteners
import tkinter as tk
from tkinter import *

# try and except to cover for error encountered if user does'nt have necessary modules installed
try:
    # Defining the processor of our url shortners, it's brain, sounds cool, I know
    def processor():
        shorten = pyshorteners.Shortener()
        shortening = shorten.gitio.short(url.get())

        short_url.set(shortening)

    # Defining the copy function to copy the shortned url
    def copy():
        pyperclip.copy( short_url.get())

     # if it is satified,   
    if __name__=="__main__":
        # Defining the User Interface
        gui = tk.Tk()
        gui.title("IJ_URL")
        gui.geometry("600x600")
        gui.configure(bg="black")

# Defining the String Variables
        url = StringVar()
        short_url= StringVar()

# Label Heading
        label = tk.Label(
            gui,
            text = "IJ URL Shortner",
            font=("Arial", 36),
            bg="black",
            fg="red",
            ).pack(fill=tk.X, pady=2)

# Text box to enter url to shortned        
        entry = tk.Entry(
           
            gui,
            textvariable=url, width =100).pack(pady=5)

# Button to use function processor        
        button = tk.Button(
            gui,
            text = "Give URL",
            font=("Arial", 18),
            bg="yellow",
            fg="black",
            command =processor,).pack(pady=2)

# Label to show shortned url
        label = tk.Label(
            gui,
            text = "Shorten URL using git.io",
            font=("Arial", 36),
            bg="black",
            fg="red",
            ).pack(fill=tk.X, pady=2)

# Text box to show the shortned url
        entry = tk.Entry(
            gui,
            textvariable=short_url, width =100).pack(pady=5)

# Button to copy shortned url
        button = tk.Button(
            gui,
            text = "Copy URL",
            font=("Arial", 18),
            bg="yellow",
            fg="black",
            command =copy,).pack(pady=2)

# Loop Continuoesly
        gui.mainloop()

# What happens if an error is encountered
except:
    print("Sorry, something went wrong")
    choice = input("Do you want to trouble shoot? (y/n): ")
    if choice=="y":
        print("Check if all necessary Modules are installed., Check for: ")
        print("Modules: ")
        print(" pyperclip: pip install pyperclip,")
        print(" pyshorteners: pip install pyshorteners")
        print("Check if you have python installed properly.")
        print("If not, get another version of this from my repository https://github.com/newtoallofthis123")
    elif choice=='n':
        print("Okay, Thanks for using. Check out my other projects at https://github.com/newtoallofthis123")

    else:
        print("Thanks for using")

# Enjoy



import pyqrcode
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import os

def qr_processor():
    image = pyqrcode.create(data1.get())
    image.png((imgname.get()), scale=10)

def open_code():
   file= filedialog.askopenfilename()
   os.system('"%s"' %file)

if __name__=="__main__":
    gui = tk.Tk(className = "NS QR")
    gui.title("NS QR Code Generator")
    photo = PhotoImage(file = "qr_icon.png")
    gui.iconphoto(False, photo)
    gui.geometry("600x600")
    gui.configure(bg="black")

    data1 = StringVar()
    imgname = StringVar()

    label = tk.Label(
        gui,
        text = "Qr-Code Generator",
        font = ("Arial", 28),
        bg = "#40FAE4",
        fg = "black",
        ).pack(pady=2)
    entry = tk.Entry(
        gui,
        textvariable=data1, width =100).pack(pady=5)
    label = tk.Label(
        gui,
        text = "QR-Code Name",
        font=("Arial", 28),
        bg="#FA4062",
        fg="black",
        ).pack(pady=2)
    entry = tk.Entry(
        gui,
        textvariable=imgname, width =100,
        ).pack(pady=5)
    button = tk.Button(
        gui,
        text = "Generate QR-Code",
        font=("Arial", 18),
        bg="#23FD71",
        fg="black",
        command =qr_processor,).pack(pady=2)
    canvas= Canvas(gui, width= 150, height= 150)
    canvas.pack()

    img= ImageTk.PhotoImage(Image.open("ns.png"))

    canvas.create_image(10,10,anchor=NW,image=img)
    label = tk.Label(
        gui,
        text = "You will find the QR-Code in the directory you stored this program",
        font = ("Arial", 18),
        bg = "black",
        fg = "#C5FFB8",
        ).pack(fill=tk.X, pady=2)
    button = tk.Button(
        gui,
        text = "Open QR-Code",
        font = ("Arial", 18),
        bg = "#C5FFB8",
        fg = "black",
        command = open_code
        ).pack(pady=2)
    label = tk.Label(
        gui,
        text = "Made by NoobScience, scan the QR-Code to see my other projects",
        font = ("Arial", 18),
        bg = "black",
        fg = "#C5FFB8",
        ).pack(fill=tk.X, pady=2)

    
    gui.mainloop()
        
        
    







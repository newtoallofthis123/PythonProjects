# Name of the Project : IJ-Speed.py
# Written by NoobScience : https://github.com/newtoallofthis123
# Modules Used : imdb (pip install speedtest)

# import the module as st
import speedtest as st
import tkinter as tk
from tkinter import *

def speedtest():
    # defining
    stn = st.Speedtest()
    # Get upload and download
    download = stn.download(dwn.get())
    upload = stn.upload(upl.get())
    #printing download and upload speeds
    print(download)
    print(upload)
    # Get Servers
    stn.get_servers([])
    # Get Ping for the Servers
    ping = stn.results.ping
    # Print ping
    print(ping)

if __name__=="__main__":
    gui = tk.Tk()
    gui.title("IJ-Speed")
    gui.geometry("300x300")
    gui.configure(bg="black")

    dwn = StringVar()
    upl = StringVar()

    label = tk.Label(
        gui,
        text = "IJ Speed Test",
        font=("Arial", 36),
        bg="black",
        fg="red",
        ).pack(fill=tk.X, pady=2)
    entry = tk.Entry(
        gui,
        textvariable=dwn, width =100).pack(pady=5)
    button = tk.Button(
        gui,
        text = "Give URL",
        font=("Arial", 18),
        bg="yellow",
        fg="black",
        command =speedtest,).pack(pady=2)



    

    
    


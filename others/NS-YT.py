from tkinter import *
from tkinter import filedialog
import os
import sys
import subprocess

#Selecting output directory
def select_output_dir():
    global token2, folder_selected
    folder_selected1 = filedialog.askdirectory()
    folder_selected = folder_selected1 + '/'
    showSelectedFolder = Label(root, text= "Downloading to the Directory " + folder_selected)
    # showSelectedFolder.pack()
    # print(folder_selected)
    token2 = True


# Getting the URL
def get_url():
    global url, url_official
    url_instructions = Label(text="Enter the URL of the video you want to Download: ")
    url_instructions.grid(row=1, column=2)
    url_official = Entry(root)
    url_official.grid(row=2, column=2)
    downloadButton = Button(root, text="Next", command=lambda: confirm_window())
    downloadButton.grid(row=3, column=3)

def confirm_window():
    global url, downloadButton2, sub_window
    url = str(url_official.get())
    # print(url)
    sub_window = Toplevel()
    sub_window.geometry('400x200')
    sub_window.geometry('+550+300')
    sub_window.title = "Confirmation to Download"
    formatCon = Label(sub_window, text="The Choosen format : " + str(formatString))
    formatCon.pack()
    urlCon = Label(sub_window, text="URL: "+ str(url)).pack()
    downloadLocationCon = Label(sub_window, text="Download location id: " + folder_selected).pack()
    downloadButton2 = Button(sub_window, text="Download", command=lambda: download_video())
    downloadButton2.pack()

#Issuing the download command with the right parameters
def download_video():
    downloadButton2.destroy()
    waitingForDownload = Label(sub_window, text= "Downloading your Video... ")
    waitingForDownload.pack()
    os.system("youtube-dl --quiet -o '" + str(folder_selected) + "%(title)s-%(id)s.%(ext)s'" + ' -f ' + formatString +  ' ' + url )
    # print("youtube-dl --quiet -o '" + str(folder_selected) + "%(title)s-%(id)s.%(ext)s'" + ' -f ' + formatString +  ' ' + url )
    waitingForDownload.destroy()
    doneDownload = Label(sub_window, text= "The Download is Done. Please close the window").pack()


# Dropdown menu for selecting format

def formats_dropdown_menu_maker():
    formatsArray = [
    "Choose a format",
    "mp4",
    "webm",
    "mp3",
    "m4a"
    ]

    variable3 = StringVar(root)
    variable3.set(formatsArray[0])
    formatsMenu = OptionMenu(root, variable3, *formatsArray)
    formatsMenu.grid(row=2, column=4)
    def callback(*a):
        global formatString
        """ oldFormatConfirmation1 = Label(root, text="")
        oldFormatConfirmation1.destroy()
        formatConfirmation1 = Label(root, text= "The chosen format is: " + variable3.get())
        formatConfirmation1.pack()
        oldFormatConfirmation1 = formatConfirmation1 """
        # print(variable3.get())
        formatString = variable3.get()
    variable3.trace("w", callback)

    # labelTest = Label(text="", font=('Helvetica', 12), fg='red')
    # labelTest.pack(side="top")

    # def callback(*args):
    #    labelTest.configure(text="The selected item is {}".format(variable3.get()))

# Creating actual window
root = Tk()
root.geometry("525x150")
root.geometry("+450+200")

# Title
root.title("NS Youtube Downloader")

# Creating a button to activate a dropdown file browser to locate the output directory
outputChoose = Button(root, text="Select output location", command=lambda: select_output_dir())
# Calling the required functions
outputChoose.grid(row=2, column=3)
get_url()
formats_dropdown_menu_maker()

# Keeping window running constantly
root.mainloop()

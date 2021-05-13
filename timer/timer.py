#! /usr/bin/env python3
from tkinter import *
import time
from playsound import playsound 

gui = Tk()
gui.geometry('400x300')
gui.resizable(True,False)

gui.config(bg='black')

sec = StringVar()
Entry(gui, textvariable=sec, width = 2, font = ("Arial", 14)).place(x=220, y=120)
sec.set('00')
mins= StringVar()
Entry(gui, textvariable = mins, width =2, font = ('Arial', 14)).place(x=180, y=120)
mins.set('00')
hrs= StringVar()
Entry(gui, textvariable = hrs, width =2, font = ('Arial', 14)).place(x=142, y=120)
hrs.set('00')

def timer():
   times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
   while times > -1:
      minute,second = (times // 60 , times % 60)
      hour =0
      if minute > 60:
         hour , minute = (minute // 60 , minute % 60)
      sec.set(second)
      mins.set(minute)
      hrs.set(hour)
      
      gui.update()
      time.sleep(1)
      if(times == 0):
         sec.set('00')
         mins.set('00')
         hrs.set('00')
         print("Timer Done, playing alarm")
         playsound("D:\Songs\Hailee Steinfeld, Alesso - Let Me Go ft. Florida Georgia Line, WATT (Official Video)-BQ_0QLL2gqI.wav")
      times -= 1
      
Label(gui, font =('Helvetica bold',22), text = 'Set the Timer',bg
='#FA8574',fg="black").place(x=105,y=70)
Button(gui, text='START', bd ='2', bg = '#FA8574', fg = "black", font =('Helvetica bold',14), command = timer).place(x=167, y=165)
gui.mainloop()

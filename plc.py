# Importing tkinter module
from tkinter import * 
from tkinter.ttk import *
  
# creating Tk window
master = Tk()
  
# setting geometry of tk window
master.geometry("200x200")
  
# button widget
b1 = Button(master, text = "Click me !")
b1.place(relx = 0, x =-10, y = 12, anchor = NE)
  
# label widget
l = Label(master, text = "I'm a Label")
l.place(anchor = NE)
  
# button widget
b2 = Button(master, text = "GFG")
b2.place(relx = 0.5, rely = 0.5, anchor = CENTER)
  
# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
mainloop()
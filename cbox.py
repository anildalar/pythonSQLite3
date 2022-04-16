from tkinter import *
from tkinter import ttk

from db2 import Database


dbo = Database('my.db');

 
root = Tk()
#root.geometry("200x150")
root.state('zoomed');
 
frame = Frame(root)
frame.pack()

noofoptions = int(input("Enter no of options you want to insert:"))
#print("no of Options is: " + noofoptions)
 
vlist = [] # empty List

for x in range(noofoptions):
    option =input(f"Enter no of option {x} :- ")
    vlist.append(option)
    #print(x);
#print(vlist)
dbo.insert(vlist)

z = dbo.select('option_tbl')

 
Combo = ttk.Combobox(frame, values = z)
Combo.set("Pick an Option")
Combo.pack(padx = 5, pady = 5)
 
root.mainloop()
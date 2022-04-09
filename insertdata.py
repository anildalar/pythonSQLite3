import tkinter
import os.path
import sqlite3
from tkinter import messagebox
from tkinter import ttk

root = tkinter.Tk()
root.resizable(width = 1, height = 1)
root.state('zoomed')

root.title("First Tkinter Window")
'''
widgets are added here
'''
''' fname = tkinter.StringVar()
lname = tkinter.StringVar()

name_label = tkinter.Label(root, text = 'FirstName', font=('calibre',10, 'bold'))
name_label.grid(row=0,column=0)

name_entry = tkinter.Entry(root,textvariable = fname, font=('calibre',10,'normal'))
name_entry.grid(row=0,column=1)

name_label2 = tkinter.Label(root, text = 'LastName', font=('calibre',10, 'bold'))
name_label2.grid(row=1,column=0)

name_entry2 = tkinter.Entry(root,textvariable = lname, font=('calibre',10,'normal'))
name_entry2.grid(row=1,column=1)

def submit():
    fn=fname.get()
    ln=lname.get()
    
    print("The fname is : " + fn)
    print("The lname is : " + ln)
        
    f = open("./a.db", "a")
    con = sqlite3.connect('./a.db')
    cur = con.cursor()
    # Create table
    
    
    cur.execute(" CREATE TABLE IF NOT EXISTS friends (fname TEXT ,lname TEXT) ");
    

    # This is the qmark style:
    cur.execute("insert into friends values (?, ?)", (fn, ln))

    messagebox.showinfo("showinfo", "Friends Saved Successfully")
    
    con.commit() 
    con.close() 

sub_btn=tkinter.Button(root,text = 'Submit', command = submit)

sub_btn.grid(row=2,column=1) '''



# Using treeview widget
treev = ttk.Treeview(root, selectmode ='browse')
 
# Calling pack method w.r.to treeview
treev.pack(side ='left')
 
# Constructing vertical scrollbar
# with treeview
verscrlbar = ttk.Scrollbar(root,
                           orient ="vertical",
                           command = treev.yview)
 
# Calling pack method w.r.to vertical
# scrollbar
verscrlbar.pack(side ='right', fill ='x')
 
# Configuring treeview
treev.configure(xscrollcommand = verscrlbar.set)
 
# Defining number of columns
treev["columns"] = ("1", "2", "3")
 
# Defining heading
treev['show'] = 'headings'
 
# Assigning the width and anchor to  the
# respective columns
treev.column("1", width = 90, anchor ='c')
treev.column("2", width = 90, anchor ='se')
treev.column("3", width = 90, anchor ='se')
 
# Assigning the heading names to the
# respective columns
treev.heading("1", text ="Name")
treev.heading("2", text ="Sex")
treev.heading("3", text ="Age")
 
# Inserting the items and their features to the
# columns built
treev.insert("", 'end', text ="L1",values =("Nidhi", "F", "25"))
treev.insert("", 'end', text ="L2",values =("Nisha", "F", "23"))
treev.insert("", 'end', text ="L3",values =("Preeti", "F", "27"))
treev.insert("", 'end', text ="L4",values =("Rahul", "M", "20"))
treev.insert("", 'end', text ="L5",values =("Sonu", "F", "18"))
treev.insert("", 'end', text ="L6",values =("Rohit", "M", "19"))
treev.insert("", 'end', text ="L7",values =("Geeta", "F", "25"))
treev.insert("", 'end', text ="L8",values =("Ankit", "M", "22"))
treev.insert("", 'end', text ="L10",values =("Mukul", "F", "25"))
treev.insert("", 'end', text ="L11",values =("Mohit", "M", "16"))
treev.insert("", 'end', text ="L12",values =("Vivek", "M", "22"))
treev.insert("", 'end', text ="L13",values =("Suman", "F", "30"))

root.mainloop()
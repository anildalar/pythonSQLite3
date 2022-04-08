import tkinter
import os.path
import sqlite3

root = tkinter.Tk()


root.title("First Tkinter Window")
'''
widgets are added here
'''
fname = tkinter.StringVar()
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
    if os.path.exists('./a.db') :
        print('Exits');
    else:
        print('Does not Exits');
        
        fn=fname.get()
        ln=lname.get()
        
        print("The fname is : " + fn)
        print("The lname is : " + ln)
           
        f = open("./a.db", "a")
        con = sqlite3.connect('./a.db')
        cur = con.cursor()
        # Create table
        cur.execute('''CREATE TABLE friends(fname text, lname text)''')
        
        # This is the qmark style:
        cur.execute("insert into friends values (?, ?)", (fn, ln))
        
        con.commit()
        con.close()
    pass

sub_btn=tkinter.Button(root,text = 'Submit', command = submit)

sub_btn.grid(row=2,column=1)

root.state('zoomed')
root.mainloop()
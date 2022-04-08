import tkinter as anil
from tkinter import messagebox
main_window = anil.Tk()

def sayHello():
    #messagebox.Function_Name(title, message [, options])
    messagebox.showinfo("This is title","This is message")

main_window.title('Counting Seconds')
button = anil.Button(main_window, text='Stop', width=25, command=sayHello)
button.pack()


main_window.mainloop()

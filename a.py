from tkinter import *
from tkinter.messagebox import showinfo # import everything from tkinter library

"""
A Python Module can contain several thing
1. Class
2. Function
3. Varaible
4. List/Dictionary/sets/Tupple
"""


window = Tk()
window.title("Welcome to OKLABS app")
#window.attributes('-fullscreen',True)
window.state('zoomed')
window.configure(background='gray')

def helloCallBack():
       showinfo( "Hello Python", "Hello World")
def helloCallBack2():
       showinfo( "Hello2Python", "Hello World2")
       
def helloCallBack3():
       showinfo( "Hello3Python", "Hello World3")

B = Button(window, text ="Hello", command = helloCallBack)

B2 = Button(window, text ="Hello2", command = helloCallBack2)
B3 = Button(window, text ="Hello3", command = helloCallBack3)

B.pack(side = RIGHT,fill = BOTH, expand = True)
B2.pack(side = RIGHT,fill = BOTH, expand = True)
#B2.place(x = 100, y = 100)
#B.grid(row=10, column=10, padx=10, pady=10)
#B2.grid(row=20, column=20, padx=10, pady=10)
#B3.grid(row=40, column=40, padx=10, pady=10)

window.mainloop()
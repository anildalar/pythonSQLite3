import tkinter as tk
# import Tkinter as tk # for Python 2.X


class MessageWindow(tk.Toplevel):
    def __init__(self, title, message):
        super().__init__()
        self.details_expanded = False
        self.title(title)
        self.geometry("300x75+{}+{}".format(self.master.winfo_x(), self.master.winfo_y()))
        self.resizable(False, False)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        tk.Label(self, text=message).grid(row=0, column=0, columnspan=3, pady=(7, 7), padx=(7, 7), sticky="ew")
        tk.Button(self, text="OK", command=self.master.destroy).grid(row=1, column=1, sticky="e")
        tk.Button(self, text="Cancel", command=self.destroy).grid(row=1, column=2, padx=(7, 7), sticky="e")

root = tk.Tk()
root.geometry("300x224")
#root.resizable(0, 0)

def yes_exit():
    print("do other stuff here then root.destroy")
    root.destroy()

def exit_root():
    MessageWindow("Quit", "Are you sure you want to quit?")

root.protocol("WM_DELETE_WINDOW", exit_root)
root.mainloop()
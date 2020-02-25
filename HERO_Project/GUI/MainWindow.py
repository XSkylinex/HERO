from tkinter import ttk
from tkinter import *
from tkinter import Menu



class MainWindows:
    window = " "

    def __init__(self):
        self.window = Tk()
        self.window.title("HERO Project")

    def vmtabs(self, vMname, information):
        tab_control = ttk.Notebook(self.window)
        tab1 = ttk.Frame(tab_control)
        tab_control.add(tab1, text=vMname)
        lbl1 = ttk.Label(tab1, text="Status:" + information)
        lbl1.grid(column=0, row=0)
        tab_control.pack(expand=1, fill='both')

    def mainloop(self):
        self.window.mainloop()



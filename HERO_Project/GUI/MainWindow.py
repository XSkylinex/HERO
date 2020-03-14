from tkinter import ttk, filedialog
from tkinter import *

from HERO_Project.Load.LoadData import LoadData


class MainWindows:
    window = " "

    def __init__(self):
        self.window = Tk()
        self.window.title("HERO Project")

        def browse_button():
            folderPath = filedialog.askdirectory()
            LoadData(folderPath+"/", self).run()

        menu = Menu(self.window)
        new_item = Menu(menu)
        new_item.add_command(label='Choose Folder', command=browse_button)
        new_item.add_separator()
        menu.add_cascade(label='File', menu=new_item)
        self.window.config(menu=menu)
        self.window.mainloop()

    def vmtabs(self, vMname, information):
        tab_control = ttk.Notebook(self.window)
        tab1 = ttk.Frame(tab_control)
        tab_control.add(tab1, text=vMname)
        lbl1 = ttk.Label(tab1, text="Status:" + information)
        lbl1.grid(column=0, row=0)
        tab_control.pack(expand=1, fill='both')

    def mainloop(self):
        self.window.mainloop()

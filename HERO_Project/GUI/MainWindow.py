from tkinter import *


class MainWindows:

    def __init__(self, projectName):
        print("MainWindows __init__")
        window = Tk()
        window.title(projectName)
        window.mainloop()

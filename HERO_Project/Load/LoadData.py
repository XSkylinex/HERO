import os

# get all files names in TestFiles directory
from HERO_Project.GUI.MainWindow import MainWindows
from HERO_Project.Load.Manipulation import Manipulation

class LoadData:
    VMsPath = " "
    vmLists = []
    window = MainWindows()

    def __init__(self):
        self.VMsPath = '/Users/alexandrmoshisnky/Desktop/HERO/HERO_Project/TestFiles/'
        self.vmLists = os.listdir(self.VMsPath)

    def printFilesNames(self):
        print(self.vmLists)

    def run(self):
        print(self.vmLists)
        for i in range(len(self.vmLists)):
            zombie = "Zombie"
            data = Manipulation.getAllDataFromFile(self.VMsPath+self.vmLists[i])
            if Manipulation.combineAll(data):
                zombie = "Not Zombie"
            self.window.vmtabs(self.vmLists[i], zombie)
        self.window.mainloop()
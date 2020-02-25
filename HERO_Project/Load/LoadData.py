import os

# get all files names in TestFiles directory

from HERO_Project.Load.Manipulation import Manipulation


class LoadData:
    VMsPath = " "
    vmLists = []

    def __init__(self, VMsPath: str, window):
        self.VMsPath = VMsPath
        self.vmLists = os.listdir(self.VMsPath)
        self.window = window

    def run(self):
        for i in range(len(self.vmLists)):
            if not self.vmLists[i].endswith(".txt"):
                continue
            zombie = "Zombie"
            data = Manipulation.getAllDataFromFile(self.VMsPath + self.vmLists[i])
            if Manipulation.combineAll(data):
                zombie = "Not Zombie"
            self.window.vmtabs(self.vmLists[i], zombie)
        self.window.mainloop()

import os

# get all files names in TestFiles directory

from HERO_Project.Hardware.CPU.CpuCheck import CpuCheck


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
            data = CpuCheck.getAllDataFromFile(self.VMsPath + self.vmLists[i])
            if CpuCheck.combineAll(data):
                zombie = "Not Zombie"
            self.window.vmtabs(self.vmLists[i], zombie)
        self.window.mainloop()


# cpu min ~ all time = idle
# cpu min !~ all time = not idle
# 0.06 0.06 0.05 0.06 0.06 0.06 0.06 0.06 != idle
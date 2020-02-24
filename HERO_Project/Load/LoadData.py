import os

# get all files names in TestFiles directory
from HERO_Project.GUI.MainWindow import MainWindows


class LoadData:
    VMsPath = " "
    VmList = []
    window = MainWindows

    def __init__(self):
        print("LoadData __init__")
        self.VMsPath = '/Users/alexandrmoshisnky/Desktop/HERO/HERO_Project/TestFiles/'
        self.VmList = os.listdir(self.VMsPath)

    def printFilesNames(self):
        print("LoadData printFilesNames")
        print(self.VmList)

    def run(self):
        print("LoadData run")
        self.window(self.VmList[0])

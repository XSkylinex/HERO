import os

class dataAccess:
    source = "file"
    path = " "

    def __init__(src, pth):
        if src == "file":
            path = pth
        # load the data sets from configuration file

    def loader(self, name, state):
        if self.source == "file":
            # insert all of the data in the file to a dictionary divided by the beginning of the line
            pass

    @classmethod
    def getOnVMs(cls):
        #TODO: Figure out how to run virsh commands

        # returns an array/list of the VM names
        pass

    @classmethod
    def getOffVMs(cls):
        # returns an array/list of the VM names
        pass

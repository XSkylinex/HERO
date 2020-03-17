import re
from datetime import datetime


class RamCheck(object):
    def __init__(self, date: datetime, ram: float):
        self.date = date
        self.ram = ram

    @classmethod
    def getAllDataFromFile(cls, ramData):  # lines = 2n line (1. date ; 2 .cpu)
        mans = []
        for i in range(0, len(ramData), 2):
            date = datetime.strptime(ramData[i].strip(), '%a %b %d %H:%M:%S %Z %Y')  # Sat Feb 29 20:48:02 IST 2020
            ram = float(re.findall(r'[-+]?\d*\.\d+|\d+', ramData[i + 1].strip())[0])  # CPU Average: %f #node cpu load 15 minutes average
            mans.append(RamCheck(date, ram))
        return mans

    @classmethod
    def isIdle(cls, mans):
        minRam = 0.10  # min(mans, key=lambda man: man.cpu).cpu  # check bug for <0.05 usage ~0.05
        count = 0
        for i in range(len(mans) - 1):
            if minRam < mans[i].ram:
                count += 1
        return f"{int((1 - (count / len(mans))) * 100)}%"

from datetime import datetime, timedelta


class Manipulation(object):
    def __init__(self, date: datetime, cpu: str):
        self.date = date
        self.cpu = cpu

    @classmethod
    def getAllDataFromFile(cls, filepath: str):  # lines = 2n line (1. date ; 2 .cpu)
        file1 = open(filepath, 'r')
        lines = file1.readlines()
        mans = []
        for i in range(0, len(lines), 2):
            date = datetime.strptime(lines[i].strip(), '%a %b %d %H:%M:%S %Z %Y')
            cpu = lines[i + 1].strip()
            mans.append(Manipulation(date, cpu))
        return mans

    @classmethod
    def isZombie(cls, mans, startDate: datetime, endDate: datetime):
        for i in range(len(mans) - 1):
            if startDate < mans[i].date and mans[i].date < endDate and mans[i].cpu != mans[i + 1].cpu:
                return True
        return False

    @classmethod
    def combineAll(cls, mans):
        isZombieBool = False
        skip = mans[0].date - timedelta(minutes=1)
        for man in mans:
            if man.date < skip:
                continue
            startDate = man.date
            endDate = startDate + timedelta(minutes=10)
            b = Manipulation.isZombie(mans, startDate, endDate)
            if b:
                skip = endDate
                isZombieBool = True

        return isZombieBool


#mans = Manipulation.getAllDataFromFile("/Users/alexandrmoshisnky/Desktop/HERO/HERO_Project/TestFiles/final_project.txt")
# print(mans[0].date)

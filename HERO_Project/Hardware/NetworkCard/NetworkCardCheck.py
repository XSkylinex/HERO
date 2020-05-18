def netCheck(data):
    pass

def makeDayAverage(data):
    pass

def cutTime(data):
    newData = []
    for line in data:
        if line.startswith("Date:"):
            newData.append(line[:16])
        else:
            newData.append(line.split('#')[0].strip())
    return newData

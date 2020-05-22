def networkCheck(data, in_min, out_min):
    data = cutTime(data)
    count = 0
    day = []
    found = False
    while data and not found:
        cur = data.pop()
        if cur.startswith('Date:'):
            newDate = cur
            found = True

    while data:
        cur = data.pop()
        if cur.startswith('Date:'):
            if cur != newDate:
                day.reverse()
                count += checkDay(day, in_min, out_min)
                day = []
                newDate = cur
        else:
            day.append(cur)
    return count


def checkDay(day, in_min, out_min):
    add = 0
    transStart = -1
    recvStart = -1
    transEnd = -1
    recvEnd = -1
    for line in day:
        if line.startswith('Network transmit:') and transStart == -1:
            transStart = int(line.split(':')[1].strip())
        if line.startswith('Network receive:') and recvStart == -1:
            recvStart = int(line.split(':')[1].strip())
        if transStart != -1 and recvStart != -1:
            break

    day.reverse()

    for line in day:
        if line.startswith('Network transmit:') and transEnd == -1:
            transEnd = int(line.split(':')[1].strip())
        if line.startswith('Network receive:') and recvEnd == -1:
            recvEnd = int(line.split(':')[1].strip())
        if transEnd != -1 and recvEnd != -1:
            break

    if transStart < transEnd and transEnd - transStart < out_min:
        add += 1
    if recvStart < recvEnd and recvEnd - recvStart < in_min:\
        add += 1
    return add


def cutTime(data):
    newData = []
    for line in data:
        if line.startswith("Date:"):
            newData.append(line[:16])
        else:
            newData.append(line.split('#')[0].strip())
    return newData

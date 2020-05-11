def bootCheck(data):
    count = 0
    data = cutTime(data)
    newDate = 'none'
    while data:
        if newDate == 'none':
            cur = data.pop()
            if cur.startswith('Date:'):
                newDate, count = bootuptimecheck(data, cur, count)
        else:
            newDate, count = bootuptimecheck(data, newDate, count)
    return count


def bootuptimecheck(data, date, count):
    add = 0
    while data:
        cur = data.pop()
        if cur.startswith('Date:') and cur != date:
            return (cur, count + add)
        if cur.startswith('Uptime'):
            if cur.split(':')[1].strip() == '0':
                add = 1
    return ('none', count + add)


def cutTime(data):
    newData = []
    for line in data:
        if line.startswith("Date:"):
            newData.append(line[:16])
        else:
            newData.append(line.split('#')[0].strip())
    return newData

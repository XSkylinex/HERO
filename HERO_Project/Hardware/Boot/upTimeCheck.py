def uptimeCheck(data):
    cur = data.pop()
    while cur.startswith('Date:') and data:
        cur = data.pop()
    if not data:
        print("error in uptime check")
        return 1
    if cur.startswith("Uptime"):
        cur = cur.split('#')[0].strip()
        try:
            updays = float(cur.split(':')[1].strip())
        except:
            updays = 0
        if updays > 40:
            return 10
        return 1
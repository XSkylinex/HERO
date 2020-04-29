class CpuCheck(object):

    @classmethod
    def getCPUData(cls, cpuData):
        minCPU = 0.05  # should be imported from the test configuration file
        count = 0
        # only brings back the cpu average lines, and from them only the number part
        cpuList = map(lambda l: (l[12:].split('#'))[0], filter(lambda line: line.startswith('CPU Average:'), cpuData))
        for cpu in cpuList:
            # if this is a cpu data line
            if float(cpu) < minCPU:
                count += 1
        # a number between 0 and 100-> if the list length is 100 and number of times the vm was idle is 70, will return 70
        # if list length is 170 and times the vm was idle is 65, will return 38.
        return (count * 100 / len(cpuData))





    #
    # def __init__(self, date: datetime, cpu: float):
    #     self.date = date
    #     self.cpu = cpu
    #
    # @classmethod
    # def getAllDataFromFile(cls, cpuData):  # lines = 2n line (1. date ; 2 .cpu)
    #     mans = []
    #     for i in range(0, len(cpuData), 2):
    #         date = datetime.strptime(cpuData[i].strip(), '%a %b %d %H:%M:%S %Z %Y')  # Sat Feb 29 20:48:02 IST 2020
    #         cpu = float(re.findall(r'[-+]?\d*\.\d+|\d+', cpuData[i + 1].strip())[
    #                         0])  # CPU Average: %f #node cpu load 15 minutes average
    #         mans.append(CpuCheck(date, cpu))
    #     return mans
    #
    #
    # @classmethod
    # def isIdle(cls, mans):
    #     minCPU = 0.05  # min(mans, key=lambda man: man.cpu).cpu  # check bug for <0.05 usage ~0.05
    #     count = 0
    #     for i in range(len(mans) - 1):
    #         if minCPU < mans[i].cpu:
    #             count += 1
    #     return f"{int((1 - (count / len(mans))) * 100)}%"
    #

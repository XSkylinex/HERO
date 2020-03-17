import re
from datetime import datetime
import testConfiguration as test_config
from Hardware.CPU.CpuCheck import CpuCheck
from Hardware.RAM.RamCheck import RamCheck

# TODO: write tests

def testVM(stats, state):
    sum = 0
    if state == "on":
        sum += cpuTest(stats['cpu']) * test_config.weights['cpu']
        #sum += netTest(stats['net']) * test_config.weights['net']
        sum += ramTest(stats['ram']) * test_config.weights['ram']
        # sum += nameTest(stats['vm_name']) * test_config.weights['name']
        # sum += uptimeTest(stats['uptime']) * test_config.weights['uptime']
        # sum += verTest(stats['ver']) * test_config.weights['ver']
        # sum += bootTest(stats['boot']) * test_config.weights['boot']
        # sum += ageTest(stats['age']) * test_config.weights['age']
    elif state == "off":
        sum += nameTest(stats['vm_name']) * test_config.weights['name']
        # sum += ageTest(stats['age']) * test_config.weights['age']
        # sum += verTest(stats['ver']) * test_config.weights['ver']
    return sum


def getVmResults(vm_name, stats, state):
    results = {}
    if state == "on":
        results['cpu'] = cpuTest(stats['cpu'])
        results['net'] = netTest(stats['net'])
        results['ram'] = ramTest(stats['ram'])
        # results['vm_name'] = nameTest(stats['vm_name'])
        # results['uptime'] = uptimeTest(stats['uptime'])
        # results['ver'] = verTest(stats['ver'])
        # results['boot'] = bootTest(stats['boot'])
        # results['age'] = ageTest(stats['age'])
    elif state == "off":
        results['vm_name'] = nameTest(stats['vm_name'])
        # results['age'] = ageTest(stats['age'])
        # results['ver'] = verTest(stats['ver'])


def cpuTest(data):
    data = CpuCheck.getAllDataFromFile(data)
    print(CpuCheck.isIdle(data))
    return 10


def bootTest(data):
    sum = 0
    data.reverse()
    up1, up2, date = bootNext(data, ' ')
    while not date == 'end':
        # todo: check if date in range. if passed the range, return sum
        sum += bootCheck(up1, up2)
        up1, up2, date = bootNext(data, up1)
    return sum


def verTest(data):
    return 10


def uptimeTest(data):
    return 10


def ageTest(data):
    return 10


def netTest(data):
    return 10


def ramTest(data):
    data = RamCheck.getAllDataFromFile(data)
    print(RamCheck.isIdle(data))
    return 10


def nameTest(data: str):
    if data in test_config.bad_names:
        return 20
    return 10


def bootNext(data, up1):
    if len(data) < 4:
        return 'end', 'end', 'end'

    if up1 == ' ':
        line = data.pop()
        while not line.startswith("Uptime"): line = data.pop()
        up1 = line

    up2 = up1
    line = data.pop()
    while not line.startswith("Uptime"): line = data.pop()
    up1 = line

    while not line.startswith("Date"): line = data.pop()
    date = line[6:]
    return up1, up2, date


def bootCheck(up1, up2):
    # up1 needs to be bigger than up2
    pass

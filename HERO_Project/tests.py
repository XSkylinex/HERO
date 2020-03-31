import re
from datetime import datetime
import HERO_Project.testConfiguration as test_config
from HERO_Project.Hardware.CPU.CpuCheck import CpuCheck
from HERO_Project.Hardware.RAM.RamCheck import RamCheck
from HERO_Project.Hardware.Boot.bootCheck import bootCheck


# TODO: write tests
# todo: all tests bring back bad results


def testVM(stats, state):
    sum = 0
    if state == "on":
        for par in test_list.values():
            sum += par['func'](stats[par['name']]) * test_config.weights[par['name']]
        sum += nameTest(stats['vm_name']) * test_config.weights['name']
    elif state == "off":
        sum += nameTest(stats['vm_name']) * test_config.weights['name']
        # sum += ageTest(stats['age']) * test_config.weights['age']
        # sum += verTest(stats['ver']) * test_config.weights['ver'] #????
    return sum


def getVmResults(vm_name, stats, state):
    results = {}
    if state == "on":
        results['cpu'] = cpuTest(stats['cpu'])
        results['nic'] = netTest(stats['nic'])
        results['ram'] = ramTest(stats['ram'])
        results['vm_name'] = nameTest(stats['vm_name'])
        # results['uptime'] = uptimeTest(stats['uptime'])
        # results['ver'] = verTest(stats['ver'])
        results['boot'] = bootTest(stats['boot'])
        # results['age'] = ageTest(stats['age'])
    elif state == "off":
        results['vm_name'] = nameTest(stats['vm_name'])
        # results['age'] = ageTest(stats['age'])
        # results['ver'] = verTest(stats['ver'])
    return results

def check():
    return 3


def cpuTest(data):
    # % that the vm is a zombie
    result = CpuCheck.getCPUData(data)
    return result


def bootTest(data):
    return bootCheck(data)


def verTest(data):
    return 10


def uptimeTest(data):
    return 10


def ageTest(data):
    return 10


def netTest(data):
    return 10


def ramTest(data):
    return RamCheck.getRamData(ramData=data)


def nameTest(data: str):
    if data in test_config.bad_names:
        return 20
    return 10


test_list = {'cpu': {'name': 'cpu', 'prefix': 'CPU Average:', 'func': cpuTest},
             'nic': {'name': 'nic', 'prefix': 'Network ', 'func': netTest},
             'ram': {'name': 'ram', 'prefix': 'Used RAM:', 'func': ramTest},
             'uptime': {'name': 'uptime', 'prefix': 'Uptime:', 'func': uptimeTest},
             'ver': {'name': 'ver', 'prefix': 'Kernel version:', 'func': verTest},
             'boot': {'name': 'boot', 'prefix': 'Uptime:', 'func': bootTest}}

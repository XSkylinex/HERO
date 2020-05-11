import re
from datetime import datetime
import HERO_Project.testConfiguration as test_config
from HERO_Project.Hardware.CPU.CpuCheck import CpuCheck
from HERO_Project.Hardware.RAM.RamCheck import RamCheck
from HERO_Project.Hardware.Boot.bootCheck import bootCheck
from HERO_Project.Hardware.Boot.upTimeCheck import uptimeCheck
from HERO_Project.Versions.VersionsCheck import VersionsCheck


# TODO: write more tests


def testVM(stats, state):
    sum = 0
    if state == "on":
        for par in test_list.values():
            sum += par['func'](stats[par['name']]) * test_config.weights[par['name']]
        sum += nameTest(stats['vm_name']) * test_config.weights['name']
    elif state == "off":
        sum += nameTest(stats['vm_name']) * test_config.weights['name']
        # sum += ageTest(stats['age']) * test_config.weights['age']
        # sum += verTest(stats['ver']) * test_config.weights['ver']
    return sum


def getVmResults(vm_name, stats, state):
    result = {}
    if state == "on":
        for par in test_list.values():
            result[par['name']] = par['func'](stats[par['name']])
    elif state == "off":
        result['vm_name'] = nameTest(stats['vm_name'])
        # result['age'] = ageTest(stats['age'])
        # result['ver'] = verTest(stats['ver'])
    return result

def check():
    return 3


def cpuTest(data):
    # % that the vm is a zombie
    result = CpuCheck.getCPUData(data)
    return result


def bootTest(data):
    return bootCheck(data)


def verTest(data):
    return VersionsCheck.getVersion(data, test_config.kernel_ver)


def uptimeTest(data):
    return uptimeCheck(data)


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
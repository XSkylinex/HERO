import re
from datetime import datetime
import configuration as config


# get the configuration data to fit the tests
# test the given data to check if its a zombie

def testVM(stats, state):
    # TODO: actually make the tests sum something with the weights
    sum = 0
    if state == "on":
        sum = sum + cpuTest(stats['cpu']) * config.weights['cpu']
        sum = sum + nicTest(stats['nic']) * config.weights['nic']
        sum = sum + ramTest(stats['ram']) * config.weights['ram']
        sum = sum + nameTest(stats['vm_name']) * config.weights['name']
    elif state == "off":
        sum = sum + nameTest(stats['vm_name']) * config.weights['name']
    return sum


def cpuTest(data):
    return 10


def ageTest(data):
    return 10


def nicTest(data):
    return 10


def ramTest(data):
    return 10


def nameTest(data: str):
    if data.startswith("test"):
        return 20
    return 10

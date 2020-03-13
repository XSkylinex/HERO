import re
from datetime import datetime
import configuration as config
import testConfiguration as test_config

# TODO: write tests

def testVM(stats, state):
    sum = 0
    if state == "on":
        sum += cpuTest(stats['cpu']) * config.weights['cpu']
        sum += netTest(stats['net']) * config.weights['net']
        sum += ramTest(stats['ram']) * config.weights['ram']
        sum += nameTest(stats['vm_name']) * config.weights['name']
        sum += uptimeTest(stats['uptime']) * config.weights['uptime']
        sum += verTest(stats['ver']) * config.weights['ver']
        sum += bootTest(stats['boot']) * config.weights['boot']
        sum += ageTest(stats['age']) * config.weights['age']
    elif state == "off":
        sum += nameTest(stats['vm_name']) * config.weights['name']
        sum += ageTest(stats['age']) * config.weights['age']
        sum += verTest(stats['ver']) * config.weights['ver']
    return sum


def cpuTest(data):
    return 10


def bootTest(data):
    return 10


def verTest(data):
    return 10


def uptimeTest(data):
    return 10


def ageTest(data):
    return 10


def nicTest(data):
    return 10


def ramTest(data):
    return 10


def nameTest(data: str):
    if data in config.bad_names:
        return 20
    return 10

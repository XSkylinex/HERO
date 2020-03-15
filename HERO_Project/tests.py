import re
from datetime import datetime
import HERO_Project.testConfiguration as test_config

# TODO: write tests

def testVM(stats, state):
    sum = 0
    if state == "on":
        sum += cpuTest(stats['cpu']) * test_config.weights['cpu']
        sum += netTest(stats['net']) * test_config.weights['net']
        sum += ramTest(stats['ram']) * test_config.weights['ram']
        sum += nameTest(stats['vm_name']) * test_config.weights['name']
        sum += uptimeTest(stats['uptime']) * test_config.weights['uptime']
        sum += verTest(stats['ver']) * test_config.weights['ver']
        sum += bootTest(stats['boot']) * test_config.weights['boot']
        sum += ageTest(stats['age']) * test_config.weights['age']
    elif state == "off":
        sum += nameTest(stats['vm_name']) * test_config.weights['name']
        sum += ageTest(stats['age']) * test_config.weights['age']
        sum += verTest(stats['ver']) * test_config.weights['ver']
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


def netTest(data):
    return 10


def ramTest(data):
    return 10


def nameTest(data: str):
    if data in test_config.bad_names:
        return 20
    return 10

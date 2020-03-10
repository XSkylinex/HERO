import re
from datetime import datetime
import configuration as config

# get the configuration data to fit the tests
# test the given data to check if its a zombie

def cpuTest(data):
    return 10

def ageTest(data):
    return 10

def nicTest(data):
    return 10

def ramTest(data):
    return 10

def nameTest(data:str):
    if data.startswith("test"):
        return 20
    return 10
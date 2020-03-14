## Test configuration ##
# Must be edited if new tests are added.
test_list = {}

# the higher the number, the more influence that test will have.
weights = {'cpu': 13, 'net': 8, 'ram': 8, 'name': 5, 'age':8, 'uptime':8, 'ver':6, 'boot':10}

# tests:
# cpu check

# network check

# ram check

# vm name check
bad_names = ['test', 'temp', 'check']

# age

# up time check

# version check
last_ver = 14.04 # last acceptable version

# boot check
boot_days = 1 # A boot in X days or less is suspicious
## Test configuration ##
# Must be edited if new tests are added.


# the higher the number, the more influence that test will have.
weights = {'cpu': 3, 'net': 3, 'ram': 3, 'name': 2, 'age':2, 'uptime':1, 'ver':2, 'boot':2}

# tests:
# cpu check

# network check
#todo: check
in_min_day_load = 10091775 # packets received
out_min_day_load = 10819578 # packets transmitted

# ram check

# vm name check
bad_names = ['test', 'temp', 'check']

# age

# up time check
up_days = 350

# version check
last_ver = 14.04 # version of linux who publish
kernel_ver = "3.10.0-1062" # Kernel version for deep understating of VM

# boot check
past_days = 10
test_list = {}

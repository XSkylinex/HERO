## configuration of HERO: ##
# polling configuration
data_polling = 15  # minutes
zombie_searching = 40  # minutes

# sensitivity configuration
threshold_on = 80
threshold_off = 40
# the higher the number, the more influence that test will have.
weights = {'cpu': 24, 'net': 33, 'ram': 23, 'name': 1, 'uptime': 1, 'ver': 2, 'boot': 2}

# general configuration
zombie_list = "zombies.txt"
real_zombie_list = "real_zombies.txt"
result_file = 'result.txt'
data_path = "./TestFiles/"
data_suffix = ".data"
project_path = "./testResults/"
whitelist_name = "whitelist.txt"

# kvm information
virtTech = 'kvm'
server_ips = ['193.106.55.43']
private_key_path = '/home/yael/.ssh/id_rsa'


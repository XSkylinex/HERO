## configuration of HERO: ##
# polling configuration
data_polling = 15  # minutes
zombie_searching = 40  # minutes

# sensitivity configuration
threshold_on = 100
threshold_off = 40
# the higher the number, the more influence that test will have.
weights = {'cpu': 13, 'net': 8, 'ram': 8, 'name': 5, 'age': 8, 'uptime': 8, 'ver': 6, 'boot': 10}

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
private_key_path = '/Users/alexandrmoshisnky/.ssh/id_rsa'

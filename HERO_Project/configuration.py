## configuration of HERO: ##
# polling configuration
data_polling = 15  # minutes
zombie_searching = 40  # minutes

# sensitivity configuration
threshold_on = 100
threshold_off = 40
# the higher the number, the more influence that test will have.
weights = {'cpu': 3, 'net': 3, 'ram': 3, 'name': 2, 'age':2, 'uptime':1, 'ver':2, 'boot':2}

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
private_key_path = 'C:/Users/jhall/ssh/id_rsa'



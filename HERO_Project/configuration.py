## configuration of HERO: ##
# polling configuration
data_polling = 15  # minutes
zombie_searching = 40  # minutes

# sensitivity configuration
threshold_on = 60
threshold_off = 40
# the higher the number, the more influence that test will have.
weights = {'cpu': 13, 'net': 8, 'ram': 8, 'name': 5, 'age':8, 'uptime':8, 'ver':6, 'boot':10}

# general configuration
result_path = "/Users/alexandrmoshisnky/Desktop/HERO/HERO_Project/zombies.txt"
data_path = "/Users/alexandrmoshisnky/Desktop/HERO/HERO_Project/TestFiles/"
data_suffix = ".txt"
project_path = "/Users/alexandrmoshisnky/Desktop/HERO/HERO_Project/HERO_Project"
white_path = "/Users/alexandrmoshisnky/Desktop/HERO/HERO_Project/whitelist.txt"

# kvm information
virtoalizator = 'kvm'
server_ips = ['193.106.55.43']
private_key_path = '/home/yael/.ssh/id_rsa'
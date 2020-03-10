## configuration of HERO: ##
# polling configuration
data_polling = 15  # minutes
zombie_searching = 40  # minutes

# sensitivity configuration
weights = {'cpu': 10, 'nic': 5}
threshold_on = 60
threshold_off = 40
# the higher the number, the more influence that test will have.
weights = {'cpu': 13, 'nic': 8, 'ram': 8, 'name': 5}

# general configuration
result_path = "/home/yael/projects/HERO/HERO_Project/zombies.txt"
data_path = "/home/yael/projects/HERO/HERO_Project/TestFiles/"
data_suffix = ".txt"
project_path = "/home/yael/projects/HERO/HERO_Project"

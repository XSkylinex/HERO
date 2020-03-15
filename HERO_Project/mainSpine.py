import HERO_Project.dataAccess as connection
import HERO_Project.tests as tests
import HERO_Project.configuration as config

if __name__ == '__main__':
    zombies = []
    conn = connection.dataAccess("file", config.data_path)

    for vm in conn.getOnVMs():
        vm_data = conn.loader(vm, "on")
        if tests.testVM(vm_data, "on") >= config.threshold_on:
            zombies.append(vm)

    for vm in conn.getOffVMs():
        vm_data = conn.loader(vm, "off")
        if tests.testVM(vm_data, "off") >= config.threshold_off:
            zombies.append(vm)

    #TODO: change when done
    print(zombies)
    # conn.saveZombies(zombies)

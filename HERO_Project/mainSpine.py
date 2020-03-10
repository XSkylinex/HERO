import dataAccess as connection
import tests as tests
import configuration as config

if __name__ == '__main__':
    zombies = []
    conn = connection.dataAccess("file", config.data_path)

    # TODO: remove whitelisted vms from lists

    for vm in connection.dataAccess.getOnVMs():
        vm_data = conn.loader(vm, "on")
        if tests.testVM(vm_data, "on") >= config.threshold_on:
            zombies.append(vm)

    for vm in connection.dataAccess.getOffVMs():
        vm_data = conn.loader(vm, "off")
        if tests.testVM(vm_data, "off") >= config.threshold_off:
            zombies.append(vm)

    print(zombies)
    # connection.dataAccess.saveZombies(zombies)

import HERO_Project.dataAccess as dataAccess
import HERO_Project.tests as tests
import HERO_Project.configuration as config


def testVM(stats, state):
    # TODO: actually make the tests sum something with the weights
    sum = 0
    if state == "on":
        tests.cpuTest(stats['cpu'])  # * the weight
        tests.nicTest(stats['nic'])
        tests.ramTest(stats['ram'])
    elif state == "off":
        pass
    return 50


if __name__ == '__main__':
    zombies = []
    conn = dataAccess("file", config.data_path)
    vms_on = dataAccess.getOnVMs()
    vms_off = dataAccess.getOffVMs()

    for vm in vms_on:
        vm_data = conn.loader(vm, "on")
        if testVM(vm_data, "on") <= config.threshold_on:
            zombies.append(vm)

    for vm in vms_off:
        vm_data = conn.loader(vm, "off")
        if testVM(vm_data, "off") <= config.threshold_off:
            zombies.append(vm)

    with open(config.result_path, 'x') as file:
        # TODO: see if overwrites the file
        file.writelines(zombies)

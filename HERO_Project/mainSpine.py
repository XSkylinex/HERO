import dataAccess
import tests
import configuration as config


def testVM(stats, state):
    # TODO: actually make the tests sum something with the weights
    sum = 0
    if state == "on":
        sum += tests.cpuTest(stats['cpu'])  * config.weights['cpu']
        sum += tests.nicTest(stats['nic'])  * config.weights['nic']
        sum += tests.ramTest(stats['ram'])  * config.weights['ram']
        sum += tests.nameTest(stats['name']) * config.weights['name']

    elif state == "off":
        sum += tests.ramTest(stats['name']) * config.weights['name']
    return sum

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

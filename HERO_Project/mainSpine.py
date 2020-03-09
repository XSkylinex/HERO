from HERO_Project.dataAccess import *
from HERO_Project.tests import *

# load stat weights as a dictionary
# load threshold
# load result path
weights = {'cpu': 10, 'nic': 5}
threshold_on = 60
threshold_off = 40
result_path = "/HERO/zombies"
data_path = "/data/"



def testVM(stats, state):
    # run the tests with the weights and sum the results
    # TODO: actually make the tests sum something
    sum = 0
    if state == "on":
        cpuTest(stats['cpu'])  # * the weight
        nicTest(stats['nic'])
        ramTest(stats['ram'])
    elif state == "off":
        pass
    return 50


if __name__ == '__main__':
    zombies = []
    conn = dataAccess("file", data_path)
    # TODO: Decide if we want one list and make a dict/tuples of the vm name and state and change the for loops as needed
    # optional at the end
    vms_all = dataAccess.getAllVMs()

    # TODO: multi processing
    for vm in vms_all:
        # get the stats(data) about the current VM into a dictionary
        vm_data = conn.loader(vm, "on")
        # run all the tests on the VM and save the return values
        if testVM(vm_data, "on") <= threshold_on:
            zombies.append(vm)

    file = open(result_path, 'x')
    file.writelines(zombies)
    file.close()

    # vms_on = dataAccess.getOnVMs()
    # vms_off = dataAccess.getOffVMs()
    #
    # for vm in vms_on:
    #     # get the stats(data) about the current VM into a dictionary
    #     vm_data = conn.loader(vm, "on")
    #     # run all the tests on the VM and save the return values
    #     if testVM(vm_data, "on") <= threshold_on:
    #         zombies.append(vm)
    #
    # for vm in vms_off:
    #     # get the stats(data) about the current VM into a dictionary
    #     vm_data = conn.loader(vm, "off")
    #     if testVM(vm_data, "off") <= threshold_off:
    #         zombies.append(vm)

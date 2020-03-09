from HERO_Project.dataAccess import *
from HERO_Project.tests import *

# load stat weights as a dictionary
# load threshold
# load result path
weights = {}
threshold_on = 60
threshold_off = 40
result_path = " "


def testVM(stats, state):
    # run the tests with the weights and sum the results
    # TODO: actually make the tests sum something
    sum = 0
    if state == "on":
        cpuTest(stats("cpu"))
        ageTest(stats("age"))
    elif state == "off":
        ageTest(stats("age"))
    return 50


if __name__ == '__main__':
    # get the necessary information about the system
    conn = dataAccess("file", "/data/")
    vms_on = dataAccess.getOnVMs()
    vms_off = dataAccess.getOffVMs()
    # TODO: Decide if we want one list and make a dict/tuples of the vm name and state and change the for loops as needed

    for vm in vms_on:
        # get the stats(data) about the current VM into a dictionary
        vm_data = conn.loader(vm, "on")
        # run all the tests on the VM and save the return values
        if testVM(vm_data, "on") <= threshold_on:
            # add the vm to the result file or wherever
            pass

    for vm in vms_off:
        # get the stats(data) about the current VM into a dictionary
        vm_data = conn.loader(vm, "off")
        # run all the tests on the VM and save the return values
        if testVM(vm_data, "off") <= threshold_off:
            # add the vm to the result file or wherever
            pass

    pass

from HERO_Project.Load.dataAccess import *

# load stat weights as a dictionary
# load threshold
# load result path
weights = {}
tests = {}
threshold_on = 60
threshold_off = 40
result_path = " "


# TODO: load stat tests as a dictionary of methods - Should this be a method or an import????

def testVM(stats, state):
    # run the tests with the weights and sum the results
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

import HERO_Project.dataAccess as dataAccess
import HERO_Project.tests as tests
import HERO_Project.configuration as config
import HERO_Project.remoteAccess as remoteAccess
import sys


def CheckEveryVM(zombies, result, vmsDict, dataConn, state):
    for (vm, ip) in vmsDict.items():
        vm_data = dataConn.loader(vm=vm, fileName=ip, state=state)
        score = tests.testVM(vm_data, state)
        # print(vm, score)
        result.append((vm, score))
        if score >= config.threshold_on:
            zombies.append(vm)


def CheckEveryServer(zombies, result, dataConn):
    for serv in config.server_ips:
        RemConn = remoteAccess.remoteConn(ip=serv, virt=config.virtTech)
        # do shutdown vms still get an ip address?

        vms = dataConn.clearVms(RemConn.getVMs('active'))
        vmsDict = RemConn.associateIps(vms)
        CheckEveryVM(zombies, result, vmsDict, dataConn, 'on')
        for vm in vms:
            if vm not in vmsDict:
                result.append((vm, "no nic"))
                zombies.append(vm)



def VmResults(vm: str, dataConn):
    # todo: make it work for not-active servers too
    for serv in config.server_ips:
        RemConn = remoteAccess.remoteConn(ip=serv, virt=config.virtTech)
        vmsDict = RemConn.associateIps(RemConn.getVMs('active'))
        if vm in vmsDict:
            print(vmsDict[vm])
            vm_data = dataConn.loader(vm=vm, fileName=vmsDict[vm], state='on')
            score = tests.testVM(vm_data, "on")
            print(score)
            print("\n")
            results = tests.getVmResults(vm, vm_data, 'on')
            print(results)
            dataConn.saveVmResults(vm_name=vm, score=score, results=results)
            return True
    return False


def getVmResult(vm: str, dataConn: dataAccess.dataAccess) -> [(str, str)]:
    for serv in config.server_ips:
        RemConn = remoteAccess.remoteConn(ip=serv, virt=config.virtTech)
        vmsDict = RemConn.associateIps(RemConn.getVMs('active'))
        if vm in vmsDict:
            vm_data = dataConn.loader(vm=vm, fileName=vmsDict[vm], state='on')
            results = tests.getVmResults(vm, vm_data, 'on')
            return results
    return


def CheckPastResults(dataConn: dataAccess.dataAccess):
    print("Training!")

    # get all zombies what the program found
    sus_zombies = dataConn.getSusZombies()

    # get all zombies what for training
    real_zombies = dataConn.getRealZombies()

    listRzVm = []
    listSusVm = []

    # convert from array triple to object
    for rzVm in real_zombies:
        arr = {}
        for (i, j) in getVmResult(rzVm, dataConn).items():
            arr[i] = j
        listRzVm.append(arr)

    # same here convert from array triple to object
    for susVm in sus_zombies:
        arr = {}
        for (i, j) in getVmResult(susVm, dataConn).items():
            arr[i] = j
        listSusVm.append(arr)

    #("list of real zombie", listRzVm)
    #("list of sus zombile", listSusVm)

    print(config.weights, "before")

    # n^2 loop for check the wight of etch Real zombie to other zombie we found
    for rzVm in listRzVm:
        # count real zombie vm parameters if zombie we found is higher and add + 1
        cpu = 0
        nic = 0
        ram = 0
        uptime = 0
        ver = 0
        boot = 0
        for susVm in listSusVm:
            if rzVm['cpu'] < susVm['cpu']:
                cpu += 1
            if rzVm['net'] < susVm['net']:
                nic += 1
            if rzVm['ram'] < susVm['ram']:
                ram += 1
            if rzVm['uptime'] < susVm['uptime']:
                uptime += 1
            if rzVm['ver'] < susVm['ver']:
                ver += 1
            if rzVm['boot'] < susVm['boot']:
                boot += 1

        len_listSusVm = len(listSusVm)
        # average real zombie lower them we found
        # if the average less them 50% less - 1 to cpu wight
        # if the average higher them 50% add + 1 to cpu wight
        # the 0.50 is default
        # admin can change the percent by the needs
        if cpu / len_listSusVm > 0.50:
            config.weights['cpu'] += 1
        elif cpu / len_listSusVm < 0.50 and cpu != 0:
            config.weights['cpu'] -= 1

        # average real zombie lower them we found
        # if the average less them 50% less - 1 to network wight
        # if the average higher them 50% add + 1 to network wight
        # the 0.50 is default
        # admin can change the percent by the needs
        if nic / len_listSusVm > 0.50:
            config.weights['net'] += 1
        elif nic / len_listSusVm < 0.50 and nic != 0:
            config.weights['net'] -= 1

        # average real zombie lower them we found
        # if the average less them 50% less - 1 to ram wight
        # if the average higher them 50% add + 1 to ram wight
        # the 0.50 is default
        # admin can change the percent by the needs
        if ram / len_listSusVm > 0.50:
            config.weights['ram'] += 1
        elif ram / len_listSusVm < 0.50 and ram != 0:
            config.weights['ram'] -= 1

        # average real zombie lower them we found
        # if the average less them 50% less - 1 to uptime wight
        # if the average higher them 50% add + 1 to uptime wight
        # the 0.50 is default
        # admin can change the percent by the needs
        if uptime / len_listSusVm > 0.50:
            config.weights['uptime'] += 1
        elif uptime / len_listSusVm < 0.50 and uptime != 0:
            config.weights['uptime'] -= 1

        # average real zombie lower them we found
        # if the average less them 50% less - 1 to version wight
        # if the average higher them 50% add + 1 to version wight
        # the 0.50 is default
        # admin can change the percent by the needs
        if ver / len_listSusVm > 0.50:
            config.weights['ver'] += 1
        elif ver / len_listSusVm < 0.50 and ver != 0:
            config.weights['ver'] -= 1

        # average real zombie lower them we found
        # if the average less them 50% less - 1 to boot wight
        # if the average higher them 50% add + 1 to boot wight
        # the 0.50 is default
        # admin can change the percent by the needs
        if boot / len_listSusVm > 0.50:
            config.weights['boot'] += 1
        elif boot / len_listSusVm < 0.50 and boot != 0:
            config.weights['boot'] -= 1

    print(config.weights)
    with open('configuration.py', 'r') as file:
        nw = ""
        for line in file.readlines():
            if not line.startswith('weights'):
                nw = nw + line
            else:
                nwe = 'weights = {'
                for key, value in config.weights.items():
                    nwe += "'{0}': {1}, ".format(key, value)
                nwe = nwe[:-2]
                nw += nwe + '}\n'
    with open('configuration.py', 'w') as file:
        file.write(nw)



if __name__ == '__main__':
    dataConn = dataAccess.dataAccess("file", config.data_path)
    if len(sys.argv) == 2:
        if sys.argv[1] == '-train' or sys.argv[1] == '-t':
            CheckPastResults(dataConn)
        if sys.argv[1] == '-help' or sys.argv[1] == '-h':
            print("HERO is a program designated to find zombie VMs - VMs that are no"
                  "longer needed and can be shutdown to free up resources."
                  "-train or -t is used to train HERO to be better at finding zombies. "
                  "     after running HERO, add the names of actual zombies found in the"
                  "     environment to the 'real_zombies' file. when running HERO it will "
                  "     to adjust the tests to the environments needs."
                  "'vm_name' is used to get the results of a specific VM. The different "
                  "     scores on the tests for the VM will be saved to a file with the "
                  "     VM name.")
        if not sys.argv[1].startswith('-'):
            if VmResults(sys.argv[1], dataConn):
                print("Success!")
            else:
                print("VM not found")
    else:
        zombies = []
        result = []

        CheckEveryServer(zombies, result, dataConn)

        # TODO: change when done
        print(zombies)
        dataConn.saveZombies(zombies)
        dataConn.saveResults(result)

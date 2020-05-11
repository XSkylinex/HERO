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
        # TODO: add inactive vms checking
        # do shutdown vms still get an ip address?

        vms = dataConn.clearVms(RemConn.getVMs('active'))
        # print(vms)
        vmsDict = RemConn.associateIps(vms)
        # print(vmsDict)
        CheckEveryVM(zombies, result, vmsDict, dataConn, 'on')


def VmResults(vm, dataConn):
    # todo: make it work for not-active servers too
    for serv in config.server_ips:
        RemConn = remoteAccess.remoteConn(ip=serv, virt=config.virtTech)
        vmsDict = RemConn.associateIps(RemConn.getVMs('active'))
        if vm in vmsDict:
            vm_data = dataConn.loader(vm=vm, fileName=vmsDict[vm], state='on')
            score = tests.testVM(vm_data, "on")
            print(score)
            print("\n")
            results = tests.getVmResults(vm, vm_data, 'on')
            print(results)
            dataConn.saveVmResults(vm_name=vm, score=score, results=results)
            return True
    return False


def CheckPastResults(dataConn):
    print("Training!")
    # sus_zombies = dataConn.getSusZombies()
    # real_zombies = dataConn.getRealZombies()
    # #todo: finish
    #
    # for vm in real_zombies:
    #     if vm not in sus_zombies:
    #         # get vm data. Add 1 to the two parameters with the highest score.
    #         pass
    # for vm in sus_zombies:
    #     if vm not in real_zombies:
    #         # get vm data. Subtract 1 to from the two parameters with the highest score.
    #         pass


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

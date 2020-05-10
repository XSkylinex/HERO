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
    #         # get vm data. Subtrack 1 to from the two parameters with the highest score.
    #         pass


if __name__ == '__main__':
    dataConn = dataAccess.dataAccess("file", config.data_path)

    if len(sys.argv) == 2:
        if sys.argv[1] == '-train':
            CheckPastResults(dataConn)
        if sys.argv[1] == '-help':
            #todo: add nice help
            print("helping!")
    else:
        zombies = []
        result = []

        CheckEveryServer(zombies, result, dataConn)

        # TODO: change when done
        print(zombies)
        dataConn.saveZombies(zombies)
        dataConn.saveResults(result)

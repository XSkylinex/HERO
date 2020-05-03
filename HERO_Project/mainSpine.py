import HERO_Project.dataAccess as dataAccess
import HERO_Project.tests as tests
import HERO_Project.configuration as config
import HERO_Project.remoteAccess as remoteAccess

if __name__ == '__main__':
    zombies = []
    result = []

    for serv in config.server_ips:
        RemConn = remoteAccess.remoteConn(ip=serv, virt=config.virtTech)
        dataConn = dataAccess.dataAccess("file", config.data_path)

        vms = dataConn.clearVms(RemConn.getVMs('active'))
        print(vms)
        vmsDict = RemConn.associateIps(vms)
        print(vmsDict)

        for (vm, ip) in vmsDict.items():
            vm_data = dataConn.loader(vm=vm, fileName=ip, state='on')
            score = tests.testVM(vm_data, "on")
            print(vm, score)
            result.append((vm, score))
            if score >= config.threshold_on:
                zombies.append(vm)

        # TODO: add inactive vms checking
        # do shutdown vms still get an ip address?

    # TODO: change when done
    print(zombies)
    dataConn.saveZombies(zombies)
    dataConn.saveResults(result)

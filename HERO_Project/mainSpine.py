import HERO_Project.dataAccess as dataAccess
import HERO_Project.tests as tests
import HERO_Project.configuration as config
import HERO_Project.remoteAccess as remoteAccess

if __name__ == '__main__':
    zombies = []
    result = []
    conn = dataAccess.dataAccess("file", config.data_path)

    for serv in config.server_ips:
        srvr = remoteAccess.remoteConn(ip=serv, virt=config.virtoalizator)

        vms = conn.clearVms(srvr.getVMs('active'))
        vmsDict = srvr.associateIps(vms)
        for (vm, ip) in vmsDict.items():
            # should be ip and not vm, because file names
            vm_data = conn.loader(vm, "on")
            score = tests.testVM(vm_data, "on")
            result.append((vm, score))
            if score >= config.threshold_on:
                zombies.append(vm)

        vms = conn.clearVms(srvr.getVMs('inactive'))
        vmsDict = srvr.associateIps(vms)
        for (vm, ip) in vmsDict.items():
            # should be ip and not vm, because file names
            vm_data = conn.loader(vm, "off")
            score = tests.testVM(vm_data, "off")
            result.append((vm, score))
            if score >= config.threshold_off:
                zombies.append(vm)

    # TODO: change when done
    print(zombies)
    conn.saveZombies(zombies)
    conn.saveResults(result)

import dataAccess as dataAccess
import tests as tests
import configuration as config
import remoteAccess as remoteAccess

if __name__ == '__main__':
    zombies = []
    result = []
    conn = dataAccess.dataAccess("file", config.data_path)

    for serv in config.server_ips:
        srvr = remoteAccess.remoteConn(ip=serv, virt=config.virtoalizator)


    for vm in srvr.getOnVMs(conn):
        vm_data = conn.loader(vm, "on")
        score = tests.testVM(vm_data, "on")
        result.append((vm, score))
        if score >= config.threshold_on:
            zombies.append(vm)

    for vm in srvr.getOffVMs(conn):
        vm_data = conn.loader(vm, "off")
        score = tests.testVM(vm_data, "off")
        result.append((vm, score))
        if score >= config.threshold_off:
            zombies.append(vm)

    # TODO: change when done
    print(zombies)
    conn.saveZombies(zombies)
    conn.saveResults(result)

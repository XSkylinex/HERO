import HERO_Project.remoteAccess as reAc
import HERO_Project.configuration as config
import subprocess
import time
import HERO_Project.dataAccess as connection
import HERO_Project.remoteAccess as remoteAcc
import HERO_Project.tests as tests
from paramiko import SSHClient, AutoAddPolicy, RSAKey
from paramiko.auth_handler import AuthenticationException, SSHException

if __name__ == '__main__':
    remConn = remoteAcc.remoteConn('193.106.55.43', 'kvm')
    dataConn = connection.dataAccess("file", config.data_path)
    zombies = []
    result = []
    # vms = dataConn.clearVms(remConn.getVMs('active'))
    vms = dataConn.clearVms(remConn.getVMs('active'))
    vmsDict = remConn.associateIps(vms)

    for (vm, ip) in vmsDict.items():
        vm_data = dataConn.loader(vm=vm, fileName=ip, state='on')
        score = tests.testVM(vm_data, "on")
        print('VM {0} ip {1}   ---   scored:{2}'.format(vm,ip, score))
        results = tests.getVmResults(vm, vm_data, 'on')
        print(results)
        print('\n')
        print('Done')


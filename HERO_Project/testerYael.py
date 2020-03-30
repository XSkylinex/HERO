import HERO_Project.remoteAccess as reAc
import HERO_Project.configuration as config
import subprocess
import time
import HERO_Project.dataAccess as connection
import HERO_Project.tests as tests
from paramiko import SSHClient, AutoAddPolicy, RSAKey
from paramiko.auth_handler import AuthenticationException, SSHException

if __name__ == '__main__':
    zombies = []
    conn = connection.dataAccess("file", config.data_path)

    vms = ['test01','test02', 'test03', 'test04', 'test05', 'test06', 'test07', 'test08', 'test09', 'test10']

    for vm in vms:
        vm_data = conn.loader(vm, "on")
        score = tests.testVM(vm_data, "on")
        print('VM {0} scored:{1}'.format(vm, score))
        results = tests.getVmResults(vm, vm_data, 'on')
        print(results)
    print('Done')

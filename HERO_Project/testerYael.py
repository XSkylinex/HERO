import remoteAccess as reAc
import configuration as config
import subprocess
import time
import dataAccess as connection
from paramiko import SSHClient, AutoAddPolicy, RSAKey
from paramiko.auth_handler import AuthenticationException, SSHException

if __name__ == '__main__':
    kvm = reAc.remoteConn(ip='193.106.55.43', virt='kvm')
    conn = connection.dataAccess("file", config.data_path)
    print("All of the vms: ")
    print(kvm.getAllVMs())
    print("All vms w/o whitelist: ")
    print(kvm.getAllVMsW(conn))
    print("On vms w/o whitelist: ")
    print(kvm.getOnVMs(conn))
    print("Off vms w/o whitelist: ")
    print(kvm.getOffVMs(conn))

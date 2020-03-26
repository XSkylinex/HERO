import time
import paramiko
import subprocess
import HERO_Project.testConfiguration as test_config
import HERO_Project.configuration as config
from paramiko import SSHClient, AutoAddPolicy, RSAKey
from paramiko.auth_handler import AuthenticationException, SSHException


class remoteConn:
    ip_addr = ''
    virt = ''

    # what do we do with the private key?
    # user name?
    # password?

    def __init__(self, ip, virt):
        self.ip_addr = ip
        self.virt = virt

        if self.virt == 'kvm':
            self.ssh = SSHClient()
            self.ssh.set_missing_host_key_policy(AutoAddPolicy())
            self.ssh.ssh_key = RSAKey.from_private_key_file(config.private_key_path)

    def executer(self, cmd):
        self.ssh.connect(hostname=self.ip_addr, username='admin')
        channel = self.ssh.invoke_shell()
        output = channel.recv(9999).decode("utf-8")
        channel.send('su - \n')
        buff = ''
        while 'Password:' not in buff:
            resp = channel.recv(9999).decode("utf-8")
            buff += resp
        channel.send('herovszombie\n')
        buff = ''
        while '#' not in buff:
            resp = channel.recv(9999).decode("utf-8")
            buff += resp
        channel.send(cmd + '\n')
        buff = ''
        while '#' not in buff:
            resp = channel.recv(9999).decode("utf-8")
            buff += resp
        channel.close()
        return buff

    def loadOnFromMachine(self, stats):
        if self.virt == 'kvm':
            pass

    def loadOff(self, stats):
        # use virsh commands to get age and how long the machine is inactive
        stats['age'] = 100
        stats['inactive'] = 40

    def getOnVMs(self, dtaccss):
        if self.virt == 'kvm':
            output = self.executer('virsh list --name')
            vms = output.split()[3:-2]
            white = dtaccss.getWhiteList()
            for vm in vms:
                if vm in white:
                    vms.remove(vm)
            return vms

    def getOffVMs(self, dtaccss):
        if self.virt == 'kvm':
            output = self.executer('virsh list --inactive --name')
            vms = output.split()[4:-2]
            white = dtaccss.getWhiteList()
            for vm in vms:
                if vm in white:
                    vms.remove(vm)
            return vms

    def getAllVMsW(self, dtaccss):
        if self.virt == 'kvm':
            output = self.executer('virsh list --all --name')
            vms = output.split()[4:-2]
            white = dtaccss.getWhiteList()
            for vm in vms:
                if vm in white:
                    vms.remove(vm)
            return vms

    def getAllVMs(self):
        if self.virt == 'kvm':
            output = self.executer('virsh list --all --name')
            vms = output.split()
            return vms[4:-2]

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

    def executer(self, cmd, channel):
        buff = ''
        if self.virt == 'kvm':
            channel.send(cmd + '\n')
            buff = ''
            while '#' not in buff:
                resp = channel.recv(9999).decode("utf-8")
                buff += resp
            channel.close()
        return buff

    def login(self):
        if self.virt == 'kvm':
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
            return channel

    def logout(self, channel):
        if self.virt == 'kvm':
            # log out of the machine
            pass

    def loadOnFromMachine(self, stats):
        if self.virt == 'kvm':
            pass

    def loadOff(self, stats):
        if self.virt == 'kvm':
            # use virsh commands to get age and how long the machine is inactive
            stats['age'] = 100
            stats['inactive'] = 40

    def getVMs(self, typ, channel=None):
        if not channel:
            channel = self.login()
        if self.virt == 'kvm':
            if typ == 'all':
                return self.executer('virsh list --all --name', channel).split()[3:-2]
            if typ == 'active':
                return self.executer('virsh list --name', channel).split()[3:-2]
            if type == 'inactive':
                return self.executer('virsh list --inactive --name', channel).split()[3:-2]

    def associateIps(self, vms):
        vmsDict = {}
        if self.virt == 'kvm':
            channel = self.login()
            output = self.executer('virsh net-dhcp-leases default', channel).split('\r\n')[3:-2]
            for line in output:
                lst = line.split('ipv4')[1][:-1].split()
                (vm, ip) = (lst[1], lst[0])
                if vm in vms:
                    vmsDict[vm] = ip.split('/')[0]
            return vmsDict

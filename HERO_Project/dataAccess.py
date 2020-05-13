import os
import subprocess

import HERO_Project.configuration as config
import HERO_Project.tests as tests


class dataAccess:
    source = "file"
    path = " "

    def __init__(self, src, pth):
        if src == "file":
            self.source = "file"
            self.path = pth

    def loader(self, vm, fileName, state):
        stats = {'vm_name': vm}
        if state == 'on':
            self.loadOnFromFile(fileName, stats)
            # self.loadOnFromMachine(stats)
        elif state == 'off':
            # self.loadOff(stats)
            pass
        return stats

    def loadOnFromFile(self, fileName, stats):
        # TODO: finish this - should be many methods? a dictionary?
        stats['state'] = 'on'
        if self.source == "file":
            # if files become too big, can be changed to .readline() with a while and another .readline at the end
            with open(self.path + fileName + config.data_suffix, 'r') as file:
                lines = file.readlines()

            for par in tests.test_list.values():
                parList = []
                for line in lines:
                    if line.startswith("Date: ") or line.startswith(par['prefix']):
                        parList.append(line)
                stats[par['name']] = parList

    def getWhiteList(self):
        if self.source == "file":
            with open(config.project_path + '/' + config.whitelist_name, 'r') as file:
                first_line_comment = file.readline()
                lines = file.readlines()
            return lines

    def clearVms(self, vms):
        lines = []
        if self.source == "file":
            with open(config.project_path + '/' + config.whitelist_name, 'r') as file:
                first_line_comment = file.readline()
                lines = file.readlines()
        for vm in vms:
            if vm in lines:
                vms.remove(vm)
        return vms

    def saveZombies(self, zombies):
        if os.path.exists(config.project_path + '/' + config.zombie_list):
            os.remove(config.project_path + '/' + config.zombie_list)
        with open(config.project_path + '/' + config.zombie_list, 'x') as file:
            file.writelines('\n'.join(zombies))
            file.write('\n')

    def getSusZombies(self) -> [str]:
        if self.source == "file":
            with open(config.project_path + '/' + config.zombie_list, 'r') as file:
                lines = file.readlines()
            return [s.rstrip('\n') for s in lines]

    def getRealZombies(self) -> [str]:
        if self.source == "file":
            with open(config.project_path + '/' + config.real_zombie_list, 'r') as file:
                first_line_comment = file.readline()
                lines = file.readlines()
            return [s.rstrip('\n') for s in lines]

    def getVM(self, vm_name):
        # todo: fix!!!!
        process = subprocess.run(['virsh', 'dominfo ' + vm_name],
                                 check=True, stdout=subprocess.PIPE, universal_newlines=True)
        info = process.stdout.strip().split('\n')
        state = filter(lambda line: line.startswith('State:'), info)[6:].strip()
        if state == 'running':
            self.loader(vm_name, 'on')
        elif state == "shut down":
            self.loader(vm_name, 'off')

    def saveVmResults(self, vm_name, score, results):
        # print('saveVmResults\t', vm_name, '\t', score, '\t', results)
        if os.path.exists(config.project_path + '/' + vm_name + '.txt'):
            os.remove(config.project_path + '/' + vm_name + '.txt')
        with open(config.project_path + '/' + vm_name + '.txt', 'x') as file:
            file.write("Final score (with weights)is: " + str(score) + '\n')
            for (key, score) in results:
                file.write('{0} = {1} \n'.format(key, score))
            file.write('\n')

    def saveResults(self, results: [(str, str)]):
        if os.path.exists(config.project_path + '/' + config.result_file):
            os.remove(config.project_path + '/' + config.result_file)
        with open(config.project_path + '/' + config.result_file, 'x') as file:
            for (vm, score) in results:
                file.write('{0} = {1} \n'.format(vm, score))
            file.write('\n')

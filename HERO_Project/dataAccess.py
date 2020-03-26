import configuration as config
import subprocess
import testConfiguration as test_config
import os
import datetime
import tests


class dataAccess:
    source = "file"
    path = " "

    def __init__(self, src, pth):
        if src == "file":
            self.source = "file"
            self.path = pth

    def loader(self, name, state):
        stats = {'vm_name': name, 'state': state}
        if state == 'on':
            self.loadOnFromFile(stats)
            # self.loadOnFromMachine(stats)
        elif state == 'off':
            # self.loadOff(stats)
            pass
        return stats

    def loadOnFromFile(self, stats):
        # TODO: finish this - should be many methods? a dictionary?
        if self.source == "file":
            # if files become too big, can be changed to .readline() with a while and another .readline at the end
            with open(self.path + stats['vm_name'] + config.data_suffix, 'r') as file:
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

    def saveZombies(self, zombies):
        if os.path.exists(config.project_path + '/' + config.zombie_list):
            os.remove(config.project_path + '/' + config.zombie_list)
        with open(config.project_path + '/' + config.zombie_list, 'x') as file:
            file.writelines('\n'.join(zombies))
            file.write('\n')

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

    def saveVmResults(self, vm_name, results):

        with open(config.result_path + '/' + vm_name, 'x') as file:
            # TODO: see if overwrites the file
            file.writelines('\n'.join(results))
            file.write('\n')

    def saveResults(self, results):
        if os.path.exists(config.project_path + '/' + config.result_file):
            os.remove(config.project_path + '/' + config.result_file)
        with open(config.project_path + '/' + config.result_file, 'x') as file:
            for (vm, score) in results:
                file.writelines('{0} = {1} \n'.format(vm, score))
            file.write('\n')

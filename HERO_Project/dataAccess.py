import HERO_Project.configuration as config
import subprocess
import HERO_Project.testConfiguration as test_config


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
            self.loadOff(stats)
        return stats

    def loadOnFromFile(self, stats):
        # TODO: finish this - should be many methods? a dictionary?
        cpu = []
        nic = []
        ram = []
        mismatch = []
        if self.source == "file":
            # if files become too big, can be changed to .readline() with a while and another .readline at the end
            with open(self.path + stats['vm_name'] + config.data_suffix, 'r') as file:
                lines = file.readlines()

            for line in lines:
                if line.startswith("Date: "):
                    # add to all the strings that care for date
                    cpu.append(line[6:])
                    nic.append(line)
                    ram.append(line[6:])

                if line.startswith("CPU Average:"):
                    cpu.append(line)
                elif line.startswith("Network "):
                    nic.append(line)
                elif line.startswith("Used RAM:"):
                    ram.append(line)
                else:
                    mismatch.append(line)

            stats['cpu'] = cpu
            stats['nic'] = nic
            stats['ram'] = ram
            stats['mismatch'] = mismatch

    def getWhiteList(self):
        if self.source == "file":
            with open(config.white_path, 'r') as file:
                first_line_comment = file.readline()
                lines = file.readlines()
            return lines.strip().split('\n')

    def saveZombies(zombies):
        with open(config.result_path, 'x') as file:
            # TODO: see if overwrites the file
            file.writelines('\n'.join(zombies))
            file.write('\n')

    def getVM(self, vm_name):
        process = subprocess.run(['virsh', 'dominfo '+vm_name],
                                 check=True, stdout=subprocess.PIPE, universal_newlines=True)
        info = process.stdout.strip().split('\n')
        state = filter(lambda line: line.startswith('State:'), info)[6:].strip()
        if state == 'running':
            self.loader(vm_name, 'on')
        elif state == "shut down":
            self.loader(vm_name, 'off')

    def saveVmResults(self,vm_name, results):
        with open(config.result_path +'/'+vm_name, 'x') as file:
            # TODO: see if overwrites the file
            file.writelines('\n'.join(results))
            file.write('\n')


import configuration as config
import subprocess
import testConfiguration as test_config


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
            self.loadOnFromMachine(stats)
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
                    cpu.append(line)
                    nic.append(line)
                    ram.append(line)

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

    def loadOnFromMachine(self, stats):
        # TODO: read informtion from the kvm
        pass

    def loadOff(self, stats):
        # TODO: finish this - should be many methods? a dictionary?
        # use virsh commands to get age and how long the machine is inactive
        stats['age'] = 100
        stats['inactive'] = 40

    def getOnVMs(self):
        process = subprocess.run(['virsh', 'list --name'],
                                 check=True, stdout=subprocess.PIPE, universal_newlines=True)
        vms = process.stdout.strip().split('\n')
        white = getWhiteList()
        return filter(lambda v: v not in white, vms)

    def getOffVMs(self):
        process = subprocess.run(['virsh', 'list --inactive --name'],
                                 check=True, stdout=subprocess.PIPE, universal_newlines=True)
        vms = process.stdout.strip().split('\n')
        white = getWhiteList()
        return filter(lambda v: v not in white, vms)

    def geAllVMs(self):
        process = subprocess.run(['virsh', 'list --all --name'],
                                 check=True, stdout=subprocess.PIPE, universal_newlines=True)
        vms = process.stdout.strip().split('\n')
        white = getWhiteList()
        return filter(lambda v: v not in white, vms)

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

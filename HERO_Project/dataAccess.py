import configuration as config


class dataAccess:
    source = "file"
    path = " "

    def __init__(self, src, pth):
        if src == "file":
            self.source = "file"
            self.path = pth
        # load the data sets from configuration file

    def loader(self, name, state):
        stats = {'vm_name': name, 'state': state}

        if state == 'on':
            self.loadOn(stats)
        if state == 'off':
            # read the virsh commands from the kvm itself
            pass
        return stats

    def loadOn(self, stats):
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

            # TODO: do we want a list or string

            stats['cpu'] = cpu
            stats['nic'] = nic
            stats['ram'] = ram
            stats['mismatch'] = mismatch

    def loadOff(self, stats):
        # TODO: finish this - should be many methods? a dictionary?
        # use virsh commands to get age and how long the machine is inactive
        stats['age'] = 100
        stats['inactive'] = 40

    @classmethod
    def getOnVMs(cls):
        # TODO: Figure out how to run virsh commands
        return (['mtest01', 'test06'])
        # returns an array/list of the VM names

    @classmethod
    def getOffVMs(cls):
        # TODO: Figure out how to run virsh commands
        # returns an array/list of the VM names
        return (['test03'])

    @classmethod
    def geAllVMs(cls):
        # TODO: Figure out how to run virsh commands
        # returns an array/list of the VM names
        return (['test03', 'test01', 'test06'])

    @classmethod
    def saveZombies(zombies):
        with open(config.result_path, 'x') as file:
            # TODO: see if overwrites the file
            file.writelines('\n'.join(zombies))
            file.write('\n')

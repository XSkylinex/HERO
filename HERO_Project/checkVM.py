import HERO_Project.dataAccess as connection
import HERO_Project.tests as tests
import HERO_Project.configuration as config
import sys

if __name__ == '__main__':
    # todo: check and finish
    conn = connection.dataAccess("file", config.data_path)
    vm_name = sys.argv[1]
    vm_stats = conn.getVM(vm_name)
    conn.saveVmResults(vm_name, tests.getVmResults(vm_name, vm_stats, vm_stats['state']))

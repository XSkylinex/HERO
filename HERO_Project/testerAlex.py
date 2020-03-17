import configuration as config
import dataAccess as connection
import tests as tests

if __name__ == '__main__':
    zombies = []
    conn = connection.dataAccess("file", config.data_path)

    vms = ['test01', 'test06']

    for vm in vms:
        vm_data = conn.loader(vm, "on")
        print('{0} : result is {1}'.format(vm, tests.testVM(vm_data, "on")))

    print('Done')

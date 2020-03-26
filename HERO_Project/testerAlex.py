import HERO_Project.configuration as config
import HERO_Project.dataAccess as connection
import HERO_Project.tests as tests

if __name__ == '__main__':
    zombies = []
    conn = connection.dataAccess("file", config.data_path)

    vms = ['test01','test02', 'test03', 'test04', 'test05', 'test06', 'test07', 'test08', 'test09', 'test10']

    for vm in vms:
        vm_data = conn.loader(vm, "on")
        print('{0} : result is {1}'.format(vm, tests.testVM(vm_data, "on")))

    print('Done')

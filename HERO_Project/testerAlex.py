import HERO_Project.configuration as config
import HERO_Project.dataAccess as connection
import HERO_Project.tests as tests

if __name__ == '__main__':
    zombies = []
    conn = connection.dataAccess("file", config.data_path)
    file = open("./webService/result/resultToWeb.txt", "w+")


    vms = ['test01','test02', 'test03', 'test04', 'test05', 'test06', 'test07', 'test08', 'test09', 'test10']

    for vm in vms:
        vm_data = conn.loader(vm, "on")
        result = tests.testVM(vm_data, "on")
        print('{0} : result is {1}'.format(vm, result))
        file.write('{0} : result is {1}'.format(vm, result) + "\n")

    file.close()

    print('Done')

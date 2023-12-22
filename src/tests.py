import time
import yaml
from handler_osm import HandlerOSM

class Tests:
    def onboarding_test1 (self):
        status = HandlerOSM()
        if status.verify_osm_status():
            print("#Test1 (Onboarding): 3 VNFd and 1 NSd")
            start = time.time()

            test1 = HandlerOSM()

            with open('src/descriptors/test1/basic_VNF1d.yaml', 'r') as file:
                data = yaml.safe_load(file)
                test1.post_vnf_packages(data)

            with open('src/descriptors/test1/basic_VNF2d.yaml', 'r') as file:
                data = yaml.safe_load(file)
                test1.post_vnf_packages(data)

            with open('src/descriptors/test1/basic_VNF-SDNd.yaml', 'r') as file:
                data = yaml.safe_load(file)
                test1.post_vnf_packages(data)

            with open('src/descriptors/test1/basic_NSD.yaml', 'r') as file:
                data = yaml.safe_load(file)
                test1.post_ns_package(data)

            test1.post_ns_instance('nsd', 'nsd', 'nsd')

            end = time.time()
            elapsed_time = end - start
            elapsed_time = round(elapsed_time, 2)

            print(f'Time elapsed: {elapsed_time}s')

    def instantiaton (self):
        '''Calculate the instantiation time'''
        print('Instantiation time - start!')

        start = time.time()
        teste = HandlerOSM()

        nsd_id = HandlerOSM()

        vim_account_id = HandlerOSM()

        print(vim_account_id.get_vim_accounts())

        teste.post_create_ns_instances(nsd_id.get_ns_packages('hackfest_basic-ns'),
                                       'first_creation',
                                       'default',
                                       vim_account_id.get_vim_accounts())
        end = time.time()

        elapsed_time = end - start

        elapsed_time = round(elapsed_time, 2)

        print('Onboarding time - end!')

        print(f'Time elapsed: {elapsed_time}s')

if __name__ == '__main__':
    test1 = Tests()
    test1.onboarding_test1()

    #
    # teste2 = Tests()
    # teste2.instantiaton()
    #
    # sub = HandlerOSM()
    #
    # # first_creation is the name of instance
    # id_subscription = sub.post_create_new_subscription('first_creation')
    #
    # print(id_subscription)
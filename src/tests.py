import handler_osm
from descriptors_constructor import DescriptorConstrutor
from handler_osm import HandlerOSM
import time

class Tests:
    def onboarding_time(self):
        '''Calculate the onboarding time'''

        print('Onboarding time - start!')
        start = time.time()

        # create a VNFd
        new_vnfd = DescriptorConstrutor.create_template_vnfd('slice_basic_vnf',
                                                             8)

        # post a VNFd package in OSM
        post = handler_osm.HandlerOSM()
        result = post.post_vnf_packages(new_vnfd)

        if not result:
            print(f"VNF not deployed!")

        nsd = DescriptorConstrutor.create_template_ns()
        post = handler_osm.HandlerOSM()
        result = post.post_ns_package(nsd)

        if not result:
            print(f" NS not deployed!")

        end = time.time()

        elapsed_time = end - start

        elapsed_time = round(elapsed_time, 2)

        print('Onboarding time - end!')

        print(f'Time elapsed: {elapsed_time}s')

    def instantiaton_time(self):
        '''Calculate the instantiation time'''
        print('Instantiation time - start!')

        start = time.time()
        teste = HandlerOSM()

        nsd_id = HandlerOSM.get_ns_packages('hackfest_basic-ns')
        # print(nsd_id)

        vim_account_id = HandlerOSM()

        id_vim = vim_account_id.get_vim_accounts()

        teste.post_create_ns_instances(nsd_id,
                                       'first_creation',
                                       'default',
                                       id_vim)
        end = time.time()

        # print(HandlerOSM.get_ns_packages('hackfest_basic-ns'))
        elapsed_time = end - start

        elapsed_time = round(elapsed_time, 2)

        print('Onboarding time - end!')

        print(f'Time elapsed: {elapsed_time}s')

if __name__ == '__main__':
    teste1 = Tests()
    teste1.onboarding_time()

    teste2 = Tests()
    teste2.instantiaton_time()



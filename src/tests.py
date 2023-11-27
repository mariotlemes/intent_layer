from descriptors_constructor import DescriptorConstrutor
import time
from handler_osm import HandlerOSM

class Tests:
    def onboarding (self):
        """Calculate the onboarding time"""

        print('Onboarding time - start!')
        start = time.time()

        # create a VNFd
        new_vnfd = DescriptorConstrutor()

        new_vnfd = new_vnfd.create_template_vnfd('slice_basic_vnf',3)

        # post a VNFd package in OSM
        post = HandlerOSM()
        result = post.post_vnf_packages(new_vnfd)

        if not result:
            print(f"VNF not deployed!")

        nsd = DescriptorConstrutor()
        post2 = HandlerOSM()

        if not post2.post_ns_package(nsd.create_template_ns()):
            print(f" NS not deployed!")

        end = time.time()

        elapsed_time = end - start

        elapsed_time = round(elapsed_time, 2)

        print('Onboarding time - end!')

        print(f'Time elapsed: {elapsed_time}s')

    def instantiaton (self):
        '''Calculate the instantiation time'''
        print('Instantiation time - start!')

        start = time.time()
        teste = HandlerOSM()

        nsd_id = HandlerOSM()

        vim_account_id = HandlerOSM()

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
    teste1 = Tests()
    teste1.onboarding()

    teste2 = Tests()
    teste2.instantiaton()

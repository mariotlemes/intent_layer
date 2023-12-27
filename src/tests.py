import time
import yaml
from handler_osm import HandlerOSM

class Tests:
    def onboarding_test1 (self):
        test1 = HandlerOSM()
        if test1.verify_osm_status():
            print("------------------------------------------------------------------------------")
            print("              #Test1 (Onboarding): 3 VNFd and 1 NSd")
            print("------------------------------------------------------------------------------")

            start = time.time()

            with open('src/descriptors/test1/basic_VNF1d.yaml', 'r') as file:
                data = yaml.safe_load(file)
                test1.post_vnf_package(data)
            with open('src/descriptors/test1/basic_VNF2d.yaml', 'r') as file:
                data = yaml.safe_load(file)
                test1.post_vnf_package(data)
            with open('src/descriptors/test1/basic_VNF-SDNd.yaml', 'r') as file:
                data = yaml.safe_load(file)
                test1.post_vnf_package(data)
            with open('src/descriptors/test1/basic_NSD.yaml', 'r') as file:
                data = yaml.safe_load(file)
                test1.post_ns_package(data)

            end = time.time()
            elapsed_time = end - start
            elapsed_time = round(elapsed_time, 2)

            print("------------------------------------------------------------------------------")
            print("                          Onboarding Results                                  ")
            print("------------------------------------------------------------------------------")
            print(f"Time elapsed: {elapsed_time}s\n")

    def instantiaton_test1 (self):
        '''Calculate the instantiation time of a Network Service'''
        test1 = HandlerOSM()
        if test1.verify_osm_status():
            print("------------------------------------------------------------------------------")
            print("        #Test1 (Instantiation):   NS instance creation and instantiation                 ")
            print("------------------------------------------------------------------------------")

            start = time.time()

            # instance create and instantiate
            test1.post_ns_instance_create_and_instantiate('nsd', 'nsd_instance', 'teste')

            #perfom subscrition to ns instance
            # test1.post_ns_subscription('nsd_instance')
            # test1.post_ns_subscription('nsd_instance')

            end = time.time()
            elapsed_time = end - start
            elapsed_time = round(elapsed_time, 2)

            print("------------------------------------------------------------------------------")
            print("                        Instantiation Results                                 ")
            print("------------------------------------------------------------------------------")
            print(f"Time elapsed: {elapsed_time}s\n")

if __name__ == '__main__':
    # VNFd/NSd onboarding and NS instantiation for slice-based VNF.
    test1 = Tests()
    test1.onboarding_test1()
    test1.instantiaton_test1()


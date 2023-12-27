import time
import yaml
from handler_osm import HandlerOSM

class Tests:
    def clean_environment(self):
        clean = HandlerOSM()
        if not clean.get_ns_instance():
            pass
            print("Nothing to clean!!")
        else:
            id = clean.get_ns_instance()
            # print(id)
            print("Cleanning...")
            clean.post_ns_instance_terminate_and_delete(id)



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
            print(f"Time elapsed: {elapsed_time}s")

            return elapsed_time

    def instantiaton_test1 (self):
        '''Calculate the instantiation time of a Network Service'''
        test1 = HandlerOSM()
        if test1.verify_osm_status():
            print("------------------------------------------------------------------------------")
            print("        #Test1 (Instantiate): NS instance - create and instantiate            ")
            print("------------------------------------------------------------------------------")

            start = time.time()

            # create and instantiate instance
            id_occurrence = test1.post_ns_instance_create_and_instantiate('nsd', 'nsd_instance',
                                                                            'a brief description')
            #
            if test1.get_ns_lcmp_op_occs(id_occurrence):
                end = time.time()

                elapsed_time = end - start
                elapsed_time = round(elapsed_time, 2)

                print("------------------------------------------------------------------------------")
                print("                        Instantiation Results                                 ")
                print("------------------------------------------------------------------------------")
                print(f"Time elapsed: {elapsed_time}s")

                return elapsed_time

if __name__ == '__main__':
    time_onboarding = []
    time_instantiate = []
    start = time.time()

    # VNFd/NSd onboarding and NS instantiation for slice-based VNF.
    for i in range (0,2):
        test1 = Tests()
        test1.clean_environment()

        time_onboarding.append(test1.onboarding_test1())
        time_instantiate.append(test1.instantiaton_test1())

    end = time.time()
    elapsed_time = end - start
    print("------------------------------------------------------------------------------")
    print(f"Test duration: {round(elapsed_time, 2)}s.")
    print("------------------------------------------------------------------------------")

    average_onboarding = sum(time_onboarding) / len(time_onboarding)
    print(f"Time onboarding (AVG - {len(time_onboarding)} tests): {round (average_onboarding, 2)}s.")
    print("------------------------------------------------------------------------------")

    average_instantiate = sum(time_instantiate)/len(time_instantiate)
    print(f"Time instantiate (AVG - {len(time_onboarding)} tests): {round(average_instantiate, 2)}s.")


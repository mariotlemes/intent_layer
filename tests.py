import time
import yaml
from handler_osm import HandlerOSM
from timer import Timer

class Tests:
    def onboarding (self):
        '''Calculate the onboarding time of VNF descriptors for test1'''
        test1 = HandlerOSM()
        if test1.verify_osm_status():
            print("------------------------------------------------------------------------------")
            print("              #Test1 (Onboarding): 3 VNFd and 1 NSd")
            print("------------------------------------------------------------------------------")

            start = time.time()
            with open('descriptors/VNF1d.yaml', 'r') as file:
                data = yaml.safe_load(file)
                # print(data)
                test1.post_vnf_package(data)
            with open('descriptors/VNF2d.yaml', 'r') as file:
                data = yaml.safe_load(file)
                test1.post_vnf_package(data)
            with open('descriptors/VNF-SDNd.yaml', 'r') as file:
                data = yaml.safe_load(file)
                test1.post_vnf_package(data)
            with open('descriptors/NSd-2VNFs.yaml', 'r') as file:
                data = yaml.safe_load(file)
                test1.post_ns_package(data)

            end = time.time()
            elapsed_time = end - start
            elapsed_time = round(elapsed_time, 2)

            # print("------------------------------------------------------------------------------")
            # print("                          Onboarding Results                                  ")
            # print("------------------------------------------------------------------------------")
            # print(f"Time elapsed: {elapsed_time}s\n")

            return elapsed_time

    def instantiaton (self, ns_name_instance):
        '''Calculate the instantiation time of a Network Service for test1'''
        test1 = HandlerOSM()
        # if test1.verify_osm_status():
        print("------------------------------------------------------------------------------")
        print("        #Test1 (Instantiate): NS instance - create and instantiate            ")
        print("------------------------------------------------------------------------------")

        start = time.time()

        # create and instantiate instance
        id_occurrence = test1.post_ns_instance_create_and_instantiate('nsd', ns_name_instance,
                                                                        'a brief description')
        #
        if test1.get_ns_lcmp_op_occs(id_occurrence):
            end = time.time()

            elapsed_time = end - start
            elapsed_time = round(elapsed_time, 2)

            # print("------------------------------------------------------------------------------")
            # print("                        Instantiation Results                                 ")
            # print("------------------------------------------------------------------------------")
            # print(f"Time elapsed: {elapsed_time}s")

            return elapsed_time
    def onboarding_and_instantiation(self, number_of_tests, name_ns_instance):
        '''
        This test calculates the average time for onboarding 3 VNFs and 1 NSd to OSM. After,
        show the average time for instantiate the Network Service Instance.
        :param number_of_tests: number of rounds
        :return: average onboarding and instantiation time
        '''
        time_onboarding = []
        time_instantiate = []

        timer = Timer()
        timer.start()

        for i in range(0, number_of_tests):
            clean = HandlerOSM()
            test1 = Tests()

            timer.pause()
            clean.clean_environment()
            timer.resume()

            time_onboarding.append(test1.onboarding())
            time_instantiate.append(test1.instantiaton(name_ns_instance))

        # end = time.time()
        # elapsed_time = end - start
        elapsed_time = timer.elapsed_time()
        # print("------------------------------------------------------------------------------")
        # print(f"                        End test1 - Results                                  ")
        print("------------------------------------------------------------------------------")
        print(f"Test duration: {round(elapsed_time, 2)}s.")
        print("------------------------------------------------------------------------------")
        average_onboarding = sum(time_onboarding) / len(time_onboarding)
        print(f"Onboarding time (AVG - {len(time_onboarding)} tests): {round(average_onboarding, 2)}s.")
        print("------------------------------------------------------------------------------")
        average_instantiate = sum(time_instantiate) / len(time_instantiate)
        print(f"Instantiating time (AVG - {len(time_onboarding)} tests): {round(average_instantiate, 2)}s.")
        print("------------------------------------------------------------------------------")
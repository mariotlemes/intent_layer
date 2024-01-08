import time
import yaml
import os
import sys
from handler_osm import HandlerOSM
from timer import Timer
from database import DataBase

path_project = os.path.abspath(os.path.join(os.getcwd()))
sys.path.append(path_project)

def load_vnf_descriptors():
    osm = HandlerOSM()
    with open('descriptors/VNF1d.yaml', 'r') as file:
        data = yaml.safe_load(file)
        osm.post_vnf_package(data)
    with open('descriptors/VNF2d.yaml', 'r') as file:
        data = yaml.safe_load(file)
        osm.post_vnf_package(data)
    with open('descriptors/VNF-SDNd.yaml', 'r') as file:
        data = yaml.safe_load(file)
        osm.post_vnf_package(data)

def onboarding(number_descriptors):
    '''Calculate the onboarding time of VNF descriptors for test1'''
    osm = HandlerOSM()
    if osm.verify_osm_status():
        print("------------------------------------------------------------------------------")
        print("              Onboarding to OSM: VNFd and NSd                                 ")
        print("------------------------------------------------------------------------------")
        if number_descriptors == 4:
            start = time.time()
            load_vnf_descriptors()
            with open('descriptors/NSd-2VNFs.yaml', 'r') as file:
                data = yaml.safe_load(file)
                osm.post_ns_package(data)

            end = time.time()
            elapsed_time = end - start
            elapsed_time = round(elapsed_time, 2)

        if number_descriptors == 5:
            start = time.time()
            load_vnf_descriptors()
            with open('descriptors/NSd-3VNFs.yaml', 'r') as file:
                data = yaml.safe_load(file)
                osm.post_ns_package(data)

            end = time.time()
            elapsed_time = end - start
            elapsed_time = round(elapsed_time, 2)

        if number_descriptors == 6:
            start = time.time()
            load_vnf_descriptors()
            with open('descriptors/NSd-4VNFs.yaml', 'r') as file:
                data = yaml.safe_load(file)
                osm.post_ns_package(data)

            end = time.time()
            elapsed_time = end - start
            elapsed_time = round(elapsed_time, 2)

        if number_descriptors == 7:
            start = time.time()
            load_vnf_descriptors()
            with open('descriptors/NSd-5VNFs.yaml', 'r') as file:
                data = yaml.safe_load(file)
                osm.post_ns_package(data)

            end = time.time()
            elapsed_time = end - start
            elapsed_time = round(elapsed_time, 2)

        if number_descriptors == 8:
            start = time.time()
            load_vnf_descriptors()
            with open('descriptors/NSd-6VNFs.yaml', 'r') as file:
                data = yaml.safe_load(file)
                osm.post_ns_package(data)

            end = time.time()
            elapsed_time = end - start
            elapsed_time = round(elapsed_time, 2)


        # print("------------------------------------------------------------------------------")
        # print("                          Onboarding Results                                  ")
        # print("------------------------------------------------------------------------------")
        # print(f"Time elapsed: {elapsed_time}s\n")

        return elapsed_time

def instantiaton(ns_name_instance):
    '''Calculate the instantiation time of a Network Service for test1'''
    osm = HandlerOSM()
    # if test1.verify_osm_status():
    print("------------------------------------------------------------------------------")
    print("                 NS instance - create and instantiate                         ")
    print("------------------------------------------------------------------------------")

    start = time.time()

    # create and instantiate instance
    id_occurrence = osm.post_ns_instance_create_and_instantiate('nsd', ns_name_instance,
                                                                    'a brief description')
    #
    if osm.get_ns_lcmp_op_occs(id_occurrence):
        end = time.time()

        elapsed_time = end - start
        elapsed_time = round(elapsed_time, 2)

        # print("------------------------------------------------------------------------------")
        # print("                        Instantiation Results                                 ")
        # print("------------------------------------------------------------------------------")
        # print(f"Time elapsed: {elapsed_time}s")

        # update intent status
        db = DataBase()
        db.update_table_intent(ns_name_instance)

        return elapsed_time
def onboarding_and_instantiation(number_of_tests, name_ns_instance, number_descriptors):
    '''
    This test calculates the average time for onboarding VNFs and NSd to OSM. After,
    show the average time for creation and instantiation the Network Service Instance.
    :param number_of_tests: number of rounds
    :return: average onboarding and instantiation time
    '''
    time_onboarding = []
    time_instantiate = []

    timer = Timer()
    timer.start()

    for i in range(0, number_of_tests):
        timer.pause()
        clean = HandlerOSM()

        # cleaning the environment
        clean.clean_environment()
        timer.resume()

        time_onboarding.append(onboarding(number_descriptors))
        time_instantiate.append(instantiaton(name_ns_instance))

    elapsed_time = timer.elapsed_time()
    # print("------------------------------------------------------------------------------")
    # print(f"                        End test1 - Results                                  ")
    # print("------------------------------------------------------------------------------")
    # print(f"Test duration: {round(elapsed_time, 2)}s.")
    print("------------------------------------------------------------------------------")
    average_onboarding = sum(time_onboarding) / len(time_onboarding)
    print(f"Onboarding time (AVG - {len(time_onboarding)} tests): {round(average_onboarding, 2)}s.")
    print("------------------------------------------------------------------------------")
    average_instantiate = sum(time_instantiate) / len(time_instantiate)
    print(f"Instantiating time (AVG - {len(time_onboarding)} tests): {round(average_instantiate, 2)}s.")
    print("------------------------------------------------------------------------------")
import time
import yaml
import os
import sys
from handler_osm import HandlerOSM
from timer import Timer
from database import DataBase

path_project = os.path.abspath(os.path.join(os.getcwd()))
sys.path.append(path_project)

history = []

def save_occurrences(id_occurrence):
    history.append(id_occurrence)
    return history

def del_occurrences():
    history.clear()

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
    '''Calculate the onboarding time of VNF/NS descriptors'''
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

    history = save_occurrences(id_occurrence)

    # for id in history:
    #     print("OCURRENCE: ", id)

    if osm.get_ns_lcmp_op_occs(id_occurrence):
        end = time.time()

        elapsed_time = end - start
        elapsed_time = round(elapsed_time, 2)

        db = DataBase()
        db.update_table_intent(ns_name_instance)

        return elapsed_time
def onboarding_and_instantiation_with_pause(number_of_tests, name_ns_instance, number_descriptors):
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

        # cleaning the environment
        clean = HandlerOSM()
        clean.clean_environment()

        timer.resume()

        time_onboarding.append(onboarding(number_descriptors))
        time_instantiate.append(instantiaton(name_ns_instance))

    print("------------------------------------------------------------------------------")
    average_onboarding = sum(time_onboarding) / len(time_onboarding)
    print(f"Onboarding time (AVG - {len(time_onboarding)} tests): {round(average_onboarding, 2)}s.")
    print("------------------------------------------------------------------------------")
    average_instantiate = sum(time_instantiate) / len(time_instantiate)
    print(f"Instantiating time (AVG - {len(time_instantiate)} tests): {round(average_instantiate, 2)}s.")
    print("------------------------------------------------------------------------------")

def onboarding_and_instantiation_without_pause(number_of_tests, name_ns_instance, number_descriptors):
    '''
    This test calculates the average time for onboarding VNFs and NSd to OSM. After,
    show the average time for creation and instantiation the Network Service Instance.
    :param number_of_tests: number of rounds
    :return: average onboarding and instantiation time
    '''

    timer_deletion = Timer()

    time_onboarding = []
    time_re_instantiation = []
    time_deletion = []
    total_time = []

    for i in range(0, number_of_tests):
        # deletion time
        timer_deletion.start()
        clean = HandlerOSM()
        clean.clean_environment()
        elapsed_time_deletion = timer_deletion.elapsed_time()

        time_deletion.append(elapsed_time_deletion)

        # re-setup time
        time_onboarding.append(onboarding(number_descriptors))
        time_re_instantiation.append(instantiaton(name_ns_instance))

        total_time.append(time_deletion[i] + time_onboarding[i] + time_re_instantiation[i])

    print("------------------------------------------------------------------------------")
    average_deleting = sum(time_deletion) / len(time_deletion)
    print(f"Deletion time (AVG - {len(time_deletion)} tests): {round(average_deleting, 2)}s.")
    print("------------------------------------------------------------------------------")

    average_onboarding = sum(time_onboarding) / len(time_onboarding)
    print(f"Onboarding time (AVG - {len(time_onboarding)} tests): {round(average_onboarding, 2)}s.")
    print("------------------------------------------------------------------------------")

    average_re_instantiate = sum(time_re_instantiation) / len(time_re_instantiation)
    print(f"Redeployment time (AVG - {len(time_re_instantiation)} tests): {round(average_re_instantiate, 2)}s.")
    print("------------------------------------------------------------------------------")

    average_total_time = sum(total_time) / len(total_time)
    print(f"Total time (AVG - {len(total_time)} tests): {round(average_total_time, 2)}s.")
    print("------------------------------------------------------------------------------")
import sys
import time
import intent_engine
import intent_gui
import intent_translator
from handler_osm import HandlerOSM
from timer import Timer
# from tests import Tests
import tests

def start_intent_gui():
    # 1 - intent_gui.py
    # create database 'system.db' if not exists
    db = intent_gui.DataBase()
    db.create_connect()
    db.create_table_intents()

    app = intent_gui.QApplication(sys.argv)

    window = intent_gui.IntentGUI()

    # status = HandlerOSM()
    # if status.verify_osm_status():
    window.show()
    app.exec()

def start_intent_engine():
    # 2 - Transform intents to NILE
    print("------------------------------------------------------------------------------")
    print("Getting starting - Translating Intent")

    objIntEngine = intent_engine.IntentEngine()

    data_from_database = objIntEngine.get_intent_from_database()

    data_transformed = objIntEngine.filling_data(data_from_database)

    nile_intent = objIntEngine.transform_to_nile(data_transformed)

    return nile_intent

def start_intent_translation(nile_intent):
    name, number_vfs = intent_translator.extract_values_from_intent(nile_intent)
    return name, number_vfs
    # intent_translator.match_nsd_descriptor(name, number_vfs)

def match_nsd_descriptor (name_intent, number_vfs):
    # print(number_vfs)
    if number_vfs == str(2):
        print("------------------------------------------------------------------------------")
        print("Getting starting - Onboarding and Instantiating Process")
        tests.onboarding_and_instantiation(1, name_intent, 4)
    if number_vfs == str(3):
        print("------------------------------------------------------------------------------")
        print("Getting starting - Onboarding and Instantiating Process")
        tests.onboarding_and_instantiation(1, name_intent, 5)
    if number_vfs == str(4):
        print("------------------------------------------------------------------------------")
        print("Getting starting - Onboarding and Instantiating Process")
        tests.onboarding_and_instantiation(1, name_intent, 6)
    if number_vfs == str(5):
        print("------------------------------------------------------------------------------")
        print("Getting starting - Onboarding and Instantiating Process")
        tests.onboarding_and_instantiation(1, name_intent, 7)
    if number_vfs == str(6):
        print("------------------------------------------------------------------------------")
        print("Getting starting - Onboarding and Instantiating Process")
        tests.onboarding_and_instantiation(1, name_intent, 8)

if __name__ == '__main__':
    start_intent_gui()

    # start intent_engine
    start = time.time()
    # timer.start()

    nile_intent = start_intent_engine()

    print(nile_intent)

    name_ns_instance, number_vfs = start_intent_translation(nile_intent)

    # print(name_ns_instance, number_vfs)
    end = time.time()

    elapsed_time = end - start

    elapsed_time = round(elapsed_time, 5)

    print(f"Translation time: {elapsed_time}")

    match_nsd_descriptor(name_ns_instance, number_vfs)





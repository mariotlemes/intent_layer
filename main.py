import sys
import intent_engine
import intent_gui
import intent_translator
from handler_osm import HandlerOSM
from timer import Timer
from tests import Tests

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
    # 2 - Transform intents to a NILE

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
    if number_vfs == '2':
        print("Starting - Onboarding and Instantiating Process")
        obj = Tests()
        obj.onboarding_and_instantiation(1, name_intent)

if __name__ == '__main__':
    start_intent_gui()

    # start intent_engine
    timer = Timer()
    timer.start()

    nile_intent = start_intent_engine()

    # print(nile_intent)

    name_ns_instance, number_vfs = start_intent_translation(nile_intent)

    # print(name_ns_instance, number_vfs)

    elapsed_time = timer.elapsed_time()

    print(f"Parsing time: {elapsed_time}")

    match_nsd_descriptor(name_ns_instance, number_vfs)





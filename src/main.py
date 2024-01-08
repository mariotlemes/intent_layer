import sys
import time
import intent_engine
import intent_gui
import intent_translator


def start_intent_gui():
    db = intent_gui.DataBase()
    db.create_connect()
    db.create_table_intents()
    app = intent_gui.QApplication(sys.argv)
    window = intent_gui.IntentGUI()
    window.show()
    app.exec()

def start_intent_engine():
    # 2 - Transform intents to NILE
    print("------------------------------------------------------------------------------")
    print("Getting starting - Translating Intent\n")
    objIntEngine = intent_engine.IntentEngine()
    data_from_database = objIntEngine.get_intent_from_database()
    not_instantiated = [tupla for tupla in data_from_database if tupla[2] == 'NOT INSTANTIATED']

    if not_instantiated:
        data_transformed = objIntEngine.filling_data(not_instantiated)
        nile_intent = objIntEngine.transform_to_nile(data_transformed)
        return nile_intent
    else:
        print("All intents deployed! Create a new intent..")
        sys.exit()

def start_intent_translation(nile_intent):
    name, number_vfs = intent_translator.extract_values_from_intent(nile_intent)
    return name, number_vfs

if __name__ == '__main__':
    start_intent_gui()



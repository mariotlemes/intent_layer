import sys

import intent_engine
import intent_gui
# import intent_translator
from handler_osm import HandlerOSM

if __name__ == '__main__':

    # 1 - intent_gui.py
    # create database 'system.db' if not exists
    db = intent_gui.DataBase()
    db.create_connect()
    db.create_table_intents()

    app = intent_gui.QApplication(sys.argv)

    window = intent_gui.IntentGUI()

    status = HandlerOSM()
    if status.verify_osm_status():
        window.show()
        app.exec()

    # 2 - Transform intents to a NILE
    objIntEngine = intent_engine.IntentEngine()

    data_list = objIntEngine.get_intents_from_database()

    data_dict = objIntEngine.parse_intent_to_dict(data_list)

    nile_intent = objIntEngine.transform_to_nile(data_dict)

    print(nile_intent)


    # if test_input == 1:
    #     window.show()
    #     app.exec()





import sqlite3, sys, os


path_project = os.path.abspath(os.path.join(os.getcwd()))
sys.path.append(path_project)

from nile.builder import build

# from nile.builder import build
class IntentEngine():
    def get_intent_from_database(self):
        """1) Get intents from database"""
        conn = sqlite3.connect('system.db')
        cursor = conn.cursor()
        cursor.execute('SELECT name, number_vfs, status FROM intents')
        intent = cursor.fetchall()
        return intent


    def filling_data (self, intent_from_database):
        name_intent = intent_from_database[0][0]
        number_vfs = intent_from_database[0][1]
        concatenated = name_intent + str(number_vfs)
        entity = {
                   'id': name_intent,
                   'middleboxes': concatenated,
                   }
        return entity

    def transform_to_nile(self, entity):
        nile_intent = build(entity)
        return nile_intent
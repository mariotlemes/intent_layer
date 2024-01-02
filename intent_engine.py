import sqlite3
from nile.builder import build

class IntentEngine():
    def get_intent_from_database(self):
        """1) Get intents in database"""
        conn = sqlite3.connect('system.db')
        cursor = conn.cursor()
        cursor.execute('SELECT name, number_vfs FROM intents')
        intent = cursor.fetchall()
        return intent


    def filling_data (self, intent_from_database):
        name_intent = intent_from_database[0][0]
        number_vfs = intent_from_database[0][1]
        concatenated = name_intent + str(number_vfs)
        entitie = {
                   'id': name_intent,
                   'middleboxes': concatenated,
                   }
        return entitie

    def transform_to_nile(self, entitie):
        nile_intent = build(entitie)
        return nile_intent








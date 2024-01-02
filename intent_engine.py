import sqlite3
from nile.builder import build

class IntentEngine():
    def get_intents_from_database(self):
        """1) Get intents in database"""
        conn = sqlite3.connect('system.db')
        cursor = conn.cursor()

        cursor.execute('SELECT name, number_vfs FROM intents')

        all_data = cursor.fetchall()

        all_data = [list(tupla) for tupla in all_data]

        return all_data

    def parse_intent_to_dict(self, intent_list):
        # transform to a dict
        dict = {item[0]: item[1] for item in intent_list}
        return dict

    def transform_to_nile(self, dict):
        dict = {'id': 'SDNslice'}
        nile_intent = build(dict)
        return nile_intent

if __name__ == '__main__':
    test = IntentEngine()
    test.get_intents_from_database()





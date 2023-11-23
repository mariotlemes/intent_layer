# from nile import compiler
from database import DataBase
import sqlite3

def get_intents_data():
    """1) Get intents in database"""
    conn = sqlite3.connect('system.db')
    cursor = conn.cursor()

    cursor.execute('SELECT name, number_vfs FROM intents')

    all_data = cursor.fetchall()

    all_data = [list(tupla) for tupla in all_data]

    return all_data


if __name__ == '__main__':
    print(get_intents_data())


    """2) Transform intents into a list"""

    """3) Call parse method:
       input: text 
       output: dictionary with intent operation targets
    """



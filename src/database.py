import sqlite3
from PySide6.QtSql import QSqlDatabase, QSqlQuery


class DataBase():
    def __init__(self, name="system.db") -> None:
        self.name = name

    def create_connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    def get_intent_from_database(self):
        """1) Get intents from database"""
        conn = sqlite3.connect('system.db')
        cursor = conn.cursor()
        cursor.execute('SELECT name, number_vfs FROM intents')
        intent = cursor.fetchall()
        return intent

    def get_status_from_intent(self):
        conn = sqlite3.connect('system.db')
        cursor = conn.cursor()
        cursor.execute('SELECT status FROM intents')
        status = cursor.fetchall()
        return status

    def insert_intent_into_database(self, name, number_vfs):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO intents(name, number_vfs) VALUES (?,?)
            """, (name, number_vfs))
            self.connection.commit()
        except AttributeError:
            print("Make the connection!")

    def create_table_intents(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                CREATE TABLE IF NOT EXISTS intents(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                    name TEXT NOT NULL UNIQUE,
                    number_vfs INTEGER NOT NULL,
                    status VARCHAR(50) DEFAULT "NOT INSTANTIATED"
                );    
            """)
        except AttributeError:
            print("Make the connection!")

    def update_table_intent(self, name_of_instance):

        if QSqlDatabase.contains('qt_sql_default_connection'):
            QSqlDatabase.removeDatabase('qt_sql_default_connection')

        # print(name_of_instance)
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("system.db")

        if not db.open():
            print("Failed to open database")
            return

        query = QSqlQuery()

        # update query
        update_query = "UPDATE intents SET status = :new_value WHERE name = :condition_value"

        # prepare the query
        query.prepare(update_query)

        query.bindValue(":condition_value", name_of_instance)
        query.bindValue(":new_value", "INSTANTIATED")

        if not query.exec_():
            print("Query execution failed:", query.lastError().text())
        else:
            db.close()
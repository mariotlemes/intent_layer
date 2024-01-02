import sqlite3
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import QHeaderView

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

    def insert_intent(self, name, number_vfs):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO intents(name, number_vfs) VALUES (?,?)
            """, (name, number_vfs))
            self.connection.commit()
        except AttributeError:
            print("faça a conexão!")

    def create_table_intents(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                CREATE TABLE IF NOT EXISTS intents(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                    name TEXT NOT NULL UNIQUE,
                    number_vfs INTEGER NOT NULL,
                    status VARCHAR(50) DEFAULT "STARTED"
                );    
            """)
        except AttributeError:
            print("faça a conexão")

    def update_table_intent(name):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("system.db")
        db.open()

        query = QSqlQuery()

        # update query
        update_query = "UPDATE intents SET status = :new_value WHERE name = :condition_value"

        # prepare the query
        query.prepare(update_query)

        # bind values to placeholders
        query.bindValue(":new_value", "DEPLOYED")  # Replace with the new value
        query.bindValue(":condition_value", name)  # Replace with the condition value

        # execute the query
        query.exec()
        db.close()

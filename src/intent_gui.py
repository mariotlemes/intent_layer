import sys
import main
import time
import intent_translator

from ui_main import Ui_MainWindow
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QHeaderView)
from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel
from PySide6.QtCore import QThread, Signal, Slot
from database import DataBase
from variables import GlobalVariables

# public ipv4 address - Open Source Mano
PUBLIC_IP_OSM = GlobalVariables.get_public_ip_osm()

@Slot()
def start_thread():
    global thread
    thread = WorkerThread()
    thread.finished.connect(thread.quit)
    thread.start()

class WorkerThread(QThread):
    finished = Signal()

    def run(self):
        # start intent_engine
        start = time.time()
        nile_intent = main.start_intent_engine()
        print(nile_intent)

        name_ns_instance, number_vfs = main.start_intent_translation(nile_intent)

        end = time.time()
        elapsed_time = end - start
        elapsed_time = round(elapsed_time, 5)
        print(f"\nTranslation time: {elapsed_time}")

        intent_translator.match_nsd_descriptor(name_ns_instance, number_vfs)

        self.finished.emit()

class CenterAlignedQueryModel(QSqlQueryModel):
    """Centering results in tw_intents QtableView"""

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter  # Align all cells to center

        return super().data(index, role)


class IntentGUI(QMainWindow, Ui_MainWindow):
    """Front-end for Intent Expressing"""

    def __init__(self):
        super(IntentGUI, self).__init__()

        self.setupUi(self)
        self.setWindowTitle("PoC - GUI-based Intent Expressing/Profiling")

        # pages
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_tables.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_table))
        self.btn_tables.clicked.connect(lambda: self.show_table_intent())
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_about))

        self.cadastrar_intent.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_intent))

        # capture action in button submit - insert intent
        self.btn_submit.clicked.connect(lambda: self.insert_intent())

        # thread to onboarding
        self.btn_submit.clicked.connect(start_thread)

        # show table intents (list of intents)
        self.show_table_intent()

    def insert_intent(self):
        """Create a new intent"""

        nome = self.txt_intent.text()
        number_of_vfs = self.txt_number_vfs.text()

        db = DataBase()
        db.create_connect()
        db.insert_intent_into_database(nome, number_of_vfs)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText("This intent was submitted with success!")
        # msg.setWindowTitle("Warning")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()
        # sys.exit()

        db.close_connection()

        # show tw_intents
        self.show_table_intent()

        # close window
        # self.close()


    def show_table_intent(self):
        """Show data from database in tw_intents QTableView"""

        if QSqlDatabase.contains('qt_sql_default_connection'):
            QSqlDatabase.removeDatabase('qt_sql_default_connection')

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("system.db")
        db.open()

        project_model = CenterAlignedQueryModel()
        project_model.setQuery("SELECT  id AS 'ID', name AS 'Name', "
                               "number_vfs AS 'Number of VFs', "
                               "status AS 'Status' FROM intents", db)
        project_view = self.tw_intents
        project_view.setModel(project_model)

        # alter spacing of column in tw_intents QTableView
        header = self.tw_intents.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.Stretch)

        # remove lines in tw_intents QTableView
        header = self.tw_intents.verticalHeader().setVisible(False)
        db.close()

    def closeEvent(self, event):
        # Ask for confirmation when closing the window
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
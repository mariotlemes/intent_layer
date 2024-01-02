from ui_main import Ui_MainWindow
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox,
                               QHeaderView)
from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel
from database import DataBase
from variables import GlobalVariables

# public ipv4 address - Open Source Mano
PUBLIC_IP_OSM = GlobalVariables.get_public_ip_osm()


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
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_about))

        self.cadastrar_intent.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_intent))

        # capture action in button submit
        self.btn_submit.clicked.connect(lambda: self.insert_intent())

        # sleep(3)

        # show table intents (list of intents)
        self.show_table_intent()

    def insert_intent(self):
        """Create a new intent"""

        nome = self.txt_intent.text()
        number_of_vfs = self.txt_number_vfs.text()

        db = DataBase()
        db.create_connect()
        db.insert_intent(nome, number_of_vfs)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText("This intent was submitted with success! Click in OK and go to List of intents")
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

        # show tw_intents
        self.show_table_intent()

        # close window
        self.close()

        # db.close_connection()

    def show_table_intent(self):
        """Show data from database in tw_intents QTableView"""

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

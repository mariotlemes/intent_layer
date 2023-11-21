# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(657, 521)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setPointSize(18)
        self.btn_home.setFont(font)
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"border-top-right-radius:15px;\n"
"border-top-left-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"background-color: rgb(255,255,255);\n"
"border: 2px;\n"
"color: black;\n"
"border -radius: 20px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #64b5f6;\n"
"    color: #fff;\n"
"	\n"
"}")
        self.btn_home.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_tables = QPushButton(self.frame)
        self.btn_tables.setObjectName(u"btn_tables")
        self.btn_tables.setMinimumSize(QSize(0, 40))
        self.btn_tables.setFont(font)
        self.btn_tables.setStyleSheet(u"QPushButton{\n"
"border-top-right-radius:15px;\n"
"border-top-left-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"background-color: rgb(255,255,255);\n"
"border: 2px;\n"
"color: black;\n"
"border -radius: 20px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #64b5f6;\n"
"    color: #fff;\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.btn_tables)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 40))
        self.btn_sobre.setFont(font)
        self.btn_sobre.setStyleSheet(u"QPushButton{\n"
"border-top-right-radius:15px;\n"
"border-top-left-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"background-color: rgb(255,255,255);\n"
"border: 2px;\n"
"color: black;\n"
"border -radius: 20px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #64b5f6;\n"
"    color: #fff;\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.btn_tables.raise_()
        self.btn_sobre.raise_()
        self.btn_home.raise_()

        self.verticalLayout.addWidget(self.frame)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.pg_table = QWidget()
        self.pg_table.setObjectName(u"pg_table")
        self.horizontalLayout_6 = QHBoxLayout(self.pg_table)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.list_intents = QWidget(self.pg_table)
        self.list_intents.setObjectName(u"list_intents")
        self.verticalLayout_2 = QVBoxLayout(self.list_intents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.txt_search = QLineEdit(self.list_intents)
        self.txt_search.setObjectName(u"txt_search")

        self.verticalLayout_2.addWidget(self.txt_search)

        self.tw_intents = QTableView(self.list_intents)
        self.tw_intents.setObjectName(u"tw_intents")
        font1 = QFont()
        font1.setPointSize(15)
        self.tw_intents.setFont(font1)

        self.verticalLayout_2.addWidget(self.tw_intents)


        self.horizontalLayout_6.addWidget(self.list_intents)

        self.Pages.addWidget(self.pg_table)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_3 = QVBoxLayout(self.pg_home)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(195, 195, 195);")

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_11 = QLabel(self.pg_home)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_2.addWidget(self.label_11)

        self.cadastrar_intent = QPushButton(self.pg_home)
        self.cadastrar_intent.setObjectName(u"cadastrar_intent")
        self.cadastrar_intent.setMinimumSize(QSize(0, 40))
        self.cadastrar_intent.setFont(font)
        self.cadastrar_intent.setStyleSheet(u"QPushButton{\n"
"border-top-right-radius:15px;\n"
"border-top-left-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"background-color: rgb(255,255,255);\n"
"border: 2px;\n"
"color: black;\n"
"border -radius: 20px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #64b5f6;\n"
"    color: #fff;\n"
"	\n"
"}")
        self.cadastrar_intent.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.cadastrar_intent)

        self.label_12 = QLabel(self.pg_home)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_2.addWidget(self.label_12)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.Pages.addWidget(self.pg_home)
        self.pg_intent = QWidget()
        self.pg_intent.setObjectName(u"pg_intent")
        self.verticalLayout_6 = QVBoxLayout(self.pg_intent)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.pg_intent)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background-color: rgb(195, 195, 195);")

        self.verticalLayout_6.addWidget(self.label_5)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.pg_intent)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.txt_intent = QLineEdit(self.pg_intent)
        self.txt_intent.setObjectName(u"txt_intent")
        self.txt_intent.setFont(font)

        self.horizontalLayout_4.addWidget(self.txt_intent)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.pg_intent)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.txt_number_vfs = QSpinBox(self.pg_intent)
        self.txt_number_vfs.setObjectName(u"txt_number_vfs")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.txt_number_vfs.sizePolicy().hasHeightForWidth())
        self.txt_number_vfs.setSizePolicy(sizePolicy1)
        self.txt_number_vfs.setFont(font)

        self.horizontalLayout_3.addWidget(self.txt_number_vfs)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.pg_intent)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.btn_submit = QPushButton(self.pg_intent)
        self.btn_submit.setObjectName(u"btn_submit")
        self.btn_submit.setMinimumSize(QSize(0, 40))
        self.btn_submit.setFont(font)
        self.btn_submit.setMouseTracking(False)
        self.btn_submit.setStyleSheet(u"QPushButton{\n"
"border-top-right-radius:15px;\n"
"border-top-left-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"background-color: rgb(255,255,255);\n"
"border: 2px;\n"
"color: black;\n"
"border -radius: 20px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #64b5f6;\n"
"    color: #fff;\n"
"	\n"
"}")
        self.btn_submit.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.btn_submit)

        self.label_9 = QLabel(self.pg_intent)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.Pages.addWidget(self.pg_intent)
        self.pg_about = QWidget()
        self.pg_about.setObjectName(u"pg_about")
        self.verticalLayout_9 = QVBoxLayout(self.pg_about)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.pg_about)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgb(195, 195, 195);")

        self.verticalLayout_7.addWidget(self.label_3)

        self.label_10 = QLabel(self.pg_about)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_7.addWidget(self.label_10)


        self.verticalLayout_9.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.pg_about)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: rgb(195, 195, 195);")

        self.verticalLayout_8.addWidget(self.label_4)

        self.label_13 = QLabel(self.pg_about)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_8.addWidget(self.label_13)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.Pages.addWidget(self.pg_about)

        self.verticalLayout.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_tables.setText(QCoreApplication.translate("MainWindow", u"List of Intents", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.txt_search.setText("")
        self.txt_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"filter...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">Network Operator</span><span style=\" font-size:36pt;\"/></p><p align=\"center\"><span style=\" font-size:24pt;\">Portal of Intent Expressing</span></p></body></html>", None))
        self.label_11.setText("")
        self.cadastrar_intent.setText(QCoreApplication.translate("MainWindow", u" New Intent", None))
        self.label_12.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Intent options</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Name of Intent:", None))
        self.txt_intent.setPlaceholderText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Number of VFs:", None))
        self.label_8.setText("")
        self.btn_submit.setText(QCoreApplication.translate("MainWindow", u"Submit Intent", None))
        self.label_9.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Demonstration</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">This is a proof of concept to demonstrate the possibility </span></p><p align=\"center\"><span style=\" font-size:18pt;\">for the network operator to submit an intention through a GUI-template</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Author</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Mario Lemes</span></p></body></html>", None))
    # retranslateUi


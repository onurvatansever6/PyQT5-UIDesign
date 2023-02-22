# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowgJzbBL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(913, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(140, 90, 671, 421))
        self.pageHome = QWidget()
        self.pageHome.setObjectName(u"pageHome")
        self.label = QLabel(self.pageHome)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 60, 331, 281))
        self.stackedWidget.addWidget(self.pageHome)
        self.pageSettings = QWidget()
        self.pageSettings.setObjectName(u"pageSettings")
        self.pushButtonNetworkSettings = QPushButton(self.pageSettings)
        self.pushButtonNetworkSettings.setObjectName(u"pushButtonNetworkSettings")
        self.pushButtonNetworkSettings.setGeometry(QRect(150, 210, 351, 71))
        self.label_2 = QLabel(self.pageSettings)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 100, 341, 101))
        self.stackedWidget.addWidget(self.pageSettings)
        self.pageNetworkSettings = QWidget()
        self.pageNetworkSettings.setObjectName(u"pageNetworkSettings")
        self.label_3 = QLabel(self.pageNetworkSettings)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 110, 431, 191))
        self.stackedWidget.addWidget(self.pageNetworkSettings)
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 90, 131, 421))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButtonHomePage = QPushButton(self.verticalLayoutWidget_2)
        self.pushButtonHomePage.setObjectName(u"pushButtonHomePage")

        self.verticalLayout_2.addWidget(self.pushButtonHomePage)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButtonSettings = QPushButton(self.verticalLayoutWidget_2)
        self.pushButtonSettings.setObjectName(u"pushButtonSettings")

        self.verticalLayout_2.addWidget(self.pushButtonSettings)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 801, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout.addWidget(self.pushButton_6)

        self.pushButton_4 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 913, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">Home Page</span></p></body></html>", None))
        self.pushButtonNetworkSettings.setText(QCoreApplication.translate("MainWindow", u"buttonNetworkSettings", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Go to Network Settings</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Network Settings</span></p></body></html>", None))
        self.pushButtonHomePage.setText(QCoreApplication.translate("MainWindow", u"buttonHomePage", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"buttonMenu", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"buttonBar", None))
        self.pushButtonSettings.setText(QCoreApplication.translate("MainWindow", u"buttonSettings", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"buttonShortcut1", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"buttonShortcut2", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"buttonSchortcut3", None))
    # retranslateUi


import sys

from PySide2.QtWidgets import *
from src.UI.Design.ui_mainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.stackedWidget.setCurrentWidget(self.ui.pageHome)
        self.ui.pushButtonHomePage.clicked.connect(self.showHomePage)
        self.ui.pushButtonSettings.clicked.connect(self.showSettingsPage)
        self.ui.pushButtonNetworkSettings.clicked.connect(self.showNetworkSettingsPage)
        self.show()

    def showHomePage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageHome)

    def showSettingsPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageSettings)

    def showNetworkSettingsPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageNetworkSettings)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

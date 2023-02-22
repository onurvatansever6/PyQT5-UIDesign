import sys

import pytest
from PySide2 import QtWidgets
from PySide2.QtGui import Qt
from PySide2.QtTest import QTest

from src.app import MainWindow


@pytest.fixture
def app():
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication()
    else:
        app = QtWidgets.QApplication.instance()
    return app


@pytest.fixture
def main_window(app):
    main_window = MainWindow()
    yield main_window
    main_window.close()


@pytest.mark.unittest
def test_show_settings_page(main_window):
    QTest.mouseClick(main_window.ui.pushButtonSettings, Qt.LeftButton)
    assert main_window.ui.stackedWidget.currentWidget() == main_window.ui.pageSettings

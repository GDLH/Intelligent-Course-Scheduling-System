import sys
import mainwindow
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from functools import partial
from PyQt5.QtCore import *
import _Administrator
import give_timetable
import qdarkstyle
import qdarkgraystyle

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    ss = QApplication(sys.argv)
    mainWindow = QMainWindow()

    ui = mainwindow.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainWindow.show()

    sys.exit(ss.exec_())


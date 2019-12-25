import sys
import mainwindow
import _Administrator
import give_timetable

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    ss = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = mainwindow.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()

    sys.exit(ss.exec_())


import sys
import mainwindow
import Students_Source

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    ss = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Students_Source.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()

    sys.exit(ss.exec_())

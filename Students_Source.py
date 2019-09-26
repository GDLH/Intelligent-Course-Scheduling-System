# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Students_Source.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 791, 541))
        self.frame.setStyleSheet("QFrame{\n"
"background:rgb(213, 255, 241)\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(300, 340, 191, 91))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.Team = QtWidgets.QComboBox(self.frame)
        self.Team.setGeometry(QtCore.QRect(150, 260, 191, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.Team.setFont(font)
        self.Team.setObjectName("Team")
        self.Team.addItem("")
        self.Team.addItem("")
        self.Team.addItem("")
        self.Team.addItem("")
        self.Team.addItem("")
        self.Major = QtWidgets.QComboBox(self.frame)
        self.Major.setGeometry(QtCore.QRect(440, 260, 231, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.Major.setFont(font)
        self.Major.setObjectName("Major")
        self.Major.addItem("")
        self.Major.addItem("")
        self.Major.addItem("")
        self.Major.addItem("")
        self.Major.addItem("")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(90, 260, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(380, 260, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "查询课表"))
        self.Team.setItemText(0, _translate("MainWindow", "29队"))
        self.Team.setItemText(1, _translate("MainWindow", "30队"))
        self.Team.setItemText(2, _translate("MainWindow", "31队"))
        self.Team.setItemText(3, _translate("MainWindow", "32队"))
        self.Team.setItemText(4, _translate("MainWindow", "33队"))
        self.Major.setItemText(0, _translate("MainWindow", "计算机科学与技术"))
        self.Major.setItemText(1, _translate("MainWindow", "软件工程"))
        self.Major.setItemText(2, _translate("MainWindow", "物联网工程"))
        self.Major.setItemText(3, _translate("MainWindow", "信息安全"))
        self.Major.setItemText(4, _translate("MainWindow", "网络工程"))
        self.label.setText(_translate("MainWindow", "队别"))
        self.label_2.setText(_translate("MainWindow", "专业"))

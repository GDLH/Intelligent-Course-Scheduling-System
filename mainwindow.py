# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
import _Administrator
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import pymysql
from functools import partial


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(631, 503)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 631, 451))
        self.frame.setStyleSheet("\n"
"QFrame{\n"
"background:rgb(255, 221, 245)\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(210, 140, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 200, 211, 31))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(240, 320, 141, 51))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(200, 50, 241, 71))
        font = QtGui.QFont()
        font.setFamily("【何尼玛】土肥圆")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(210, 260, 115, 19))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(280, 260, 115, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_3.setGeometry(QtCore.QRect(350, 260, 115, 19))
        self.radioButton_3.setObjectName("radioButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        userinfo = self.conn()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(lambda :self.onClickButton(userinfo))

    def onClickButton(self,userinfo):

        user = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if((self.radioButton.isChecked() or self.radioButton_2.isChecked() or self.radioButton_3.isChecked()) == False):
            QMessageBox.warning(self, 'warning', '请选择身份')
        else:
            if(self.radioButton.isChecked()):
                ID = '1'
            elif(self.radioButton_2.isChecked()):
                ID = '2'
            elif(self.radioButton_3.isChecked()):
                ID = '0'

            flag = 1
            for a in range(len(userinfo)):
                if (user == userinfo[a][0] and password == userinfo[a][1] and ID == userinfo[a][2]):
                    flag = 0
                    self.succeed()
                    break
                elif (user == userinfo[a][0] and (password != userinfo[a][1] or ID != userinfo[a][2])):
                    flag = 0
                    QMessageBox.warning(self, 'warning', '密码错误或身份不匹配')
                    break
            if(flag):
                QMessageBox.warning(self, 'warning', '用户不存在')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "UserName"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.label.setText(_translate("MainWindow", "智能排课系统"))
        self.radioButton.setText(_translate("MainWindow", "学生"))
        self.radioButton_2.setText(_translate("MainWindow", "教师"))
        self.radioButton_3.setText(_translate("MainWindow", "管理员"))

    def conn(self):

        # 连接数据库
        db = pymysql.connect("localhost", "root", "password", "cource_arranged_system")

        # 获取游标、数据
        cur = db.cursor()
        cur.execute("select * from signincheck")
        data = cur.fetchall()

        row = len(data)
        vol = len(data[0])

        userinfo = data
        return  userinfo




    def succeed(self):
        self.mainWindow = QMainWindow()
        ui = _Administrator.Ui_Administrator()
        ui.setupUi(self.mainWindow)
        self.mainWindow.show()
        self.close()


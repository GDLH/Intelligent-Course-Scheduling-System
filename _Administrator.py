# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_Administrator.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from functools import partial
from PyQt5.QtCore import *
import time,datetime
import give_timetable
import courcetable



class Ui_Administrator(object):
    def setupUi(self, Administrator):
        Administrator.setObjectName("Administrator")
        Administrator.resize(1391, 650)
        self.Button_Cource_Require = QtWidgets.QPushButton(Administrator)
        self.Button_Cource_Require.setGeometry(QtCore.QRect(1280, 60, 81, 151))
        self.Button_Cource_Require.setObjectName("Button_Cource_Require")
        self.Source_Table = QtWidgets.QTableWidget(Administrator)
        self.Source_Table.setGeometry(QtCore.QRect(10, 10, 1241, 261))
        self.Source_Table.setObjectName("Source_Table")
        self.Source_Table.setColumnCount(9)
        self.Source_Table.setRowCount(20)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.Source_Table.setHorizontalHeaderItem(8, item)
        self.frame = QtWidgets.QFrame(Administrator)
        self.frame.setGeometry(QtCore.QRect(10, 290, 761, 241))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 41, 20))
        self.label.setObjectName("label")
        self.Course_Name = QtWidgets.QLineEdit(self.frame)
        self.Course_Name.setGeometry(QtCore.QRect(80, 20, 113, 21))
        self.Course_Name.setObjectName("Course_Name")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 41, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(5, 170, 71, 20))
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(220, 20, 41, 20))
        self.label_4.setObjectName("label_4")
        self.Course_hours = QtWidgets.QSpinBox(self.frame)
        self.Course_hours.setGeometry(QtCore.QRect(80, 100, 46, 22))
        self.Course_hours.setObjectName("Course_hours")
        self.Course_Teacher = QtWidgets.QLineEdit(self.frame)
        self.Course_Teacher.setGeometry(QtCore.QRect(280, 20, 113, 21))
        self.Course_Teacher.setObjectName("Course_Teacher")
        self.Course_Major = QtWidgets.QLineEdit(self.frame)
        self.Course_Major.setGeometry(QtCore.QRect(280, 100, 113, 21))
        self.Course_Major.setObjectName("Course_Major")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(220, 100, 41, 21))
        self.label_5.setTextFormat(QtCore.Qt.PlainText)
        self.label_5.setObjectName("label_5")
        self.Course_Start = QtWidgets.QLineEdit(self.frame)
        self.Course_Start.setGeometry(QtCore.QRect(500, 100, 113, 21))
        self.Course_Start.setObjectName("Course_Start")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(410, 100, 71, 21))
        self.label_7.setTextFormat(QtCore.Qt.PlainText)
        self.label_7.setObjectName("label_7")
        self.Course_End = QtWidgets.QLineEdit(self.frame)
        self.Course_End.setGeometry(QtCore.QRect(500, 170, 113, 21))
        self.Course_End.setText("")
        self.Course_End.setObjectName("Course_End")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(410, 170, 71, 21))
        self.label_8.setTextFormat(QtCore.Qt.PlainText)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(410, 20, 71, 21))
        self.label_9.setTextFormat(QtCore.Qt.PlainText)
        self.label_9.setObjectName("label_9")
        self.Course_Single_hours = QtWidgets.QComboBox(self.frame)
        self.Course_Single_hours.setGeometry(QtCore.QRect(500, 20, 111, 22))
        self.Course_Single_hours.setObjectName("Course_Single_hours")
        self.Course_Single_hours.addItem("")
        self.Course_Single_hours.addItem("")
        self.Course_Single_hours.addItem("")
        self.Button_Course_Add = QtWidgets.QPushButton(self.frame)
        self.Button_Course_Add.setGeometry(QtCore.QRect(640, 20, 93, 28))
        self.Button_Course_Add.setObjectName("Button_Course_Add")
        self.Button_Course_Delete = QtWidgets.QPushButton(self.frame)
        self.Button_Course_Delete.setGeometry(QtCore.QRect(640, 100, 93, 28))
        self.Button_Course_Delete.setObjectName("Button_Course_Delete")
        self.Button_Course_Edit = QtWidgets.QPushButton(self.frame)
        self.Button_Course_Edit.setGeometry(QtCore.QRect(640, 170, 93, 28))
        self.Button_Course_Edit.setObjectName("Button_Course_Edit")
        self.Course_Type = QtWidgets.QComboBox(self.frame)
        self.Course_Type.setGeometry(QtCore.QRect(280, 170, 111, 22))
        self.Course_Type.setObjectName("Course_Type")
        self.Course_Type.addItem("")
        self.Course_Type.addItem("")
        self.Course_Type.addItem("")
        self.Course_Type.addItem("")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(220, 170, 41, 21))
        self.label_10.setTextFormat(QtCore.Qt.PlainText)
        self.label_10.setObjectName("label_10")
        self.Course_Classroom = QtWidgets.QComboBox(self.frame)
        self.Course_Classroom.setGeometry(QtCore.QRect(80, 170, 111, 22))
        self.Course_Classroom.setObjectName("Course_Classroom")
        self.Course_Classroom.addItem("")
        self.Course_Classroom.addItem("")
        self.Course_Classroom.addItem("")
        self.Button_Quit = QtWidgets.QPushButton(Administrator)
        self.Button_Quit.setGeometry(QtCore.QRect(20, 540, 181, 51))
        self.Button_Quit.setObjectName("Button_Quit")
        self.label_6 = QtWidgets.QLabel(Administrator)
        self.label_6.setGeometry(QtCore.QRect(270, 550, 500, 50))
        font = QtGui.QFont()
        font.setFamily("【何尼玛】土肥圆")
        font.setPointSize(28)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.frame_2 = QtWidgets.QFrame(Administrator)
        self.frame_2.setGeometry(QtCore.QRect(880, 290, 480, 311))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Course_List = QtWidgets.QListWidget(self.frame_2)
        self.Course_List.setGeometry(QtCore.QRect(30, 20, 256, 192))
        self.Course_List.setObjectName("Course_List")
        self.Course_Choose = QtWidgets.QComboBox(self.frame_2)
        self.Course_Choose.setGeometry(QtCore.QRect(290, 20, 161, 31))
        self.Course_Choose.setObjectName("Course_Choose")
        self.Button_Add = QtWidgets.QPushButton(self.frame_2)
        self.Button_Add.setGeometry(QtCore.QRect(290, 60, 161, 28))
        self.Button_Add.setObjectName("Button_Add")
        self.Button_Delete = QtWidgets.QPushButton(self.frame_2)
        self.Button_Delete.setGeometry(QtCore.QRect(290, 100, 161, 28))
        self.Button_Delete.setObjectName("Button_Delete")
        self.Button_List_Create = QtWidgets.QPushButton(self.frame_2)
        self.Button_List_Create.setGeometry(QtCore.QRect(20, 230, 111, 28))
        self.Button_List_Create.setObjectName("Button_List_Create")
        self.Button_List_Require = QtWidgets.QPushButton(self.frame_2)
        self.Button_List_Require.setGeometry(QtCore.QRect(170, 230, 111, 28))
        self.Button_List_Require.setObjectName("Button_List_Require")
        self.Start_time = QtWidgets.QLineEdit(self.frame_2)
        self.Start_time.setGeometry(QtCore.QRect(290, 140, 161, 31))
        self.Start_time.setObjectName("Start_time")
        self.End_time = QtWidgets.QLineEdit(self.frame_2)
        self.End_time.setGeometry(QtCore.QRect(290, 180, 161, 31))
        self.End_time.setObjectName("End_time")
        self.label.setBuddy(self.Course_Name)

        self.retranslateUi(Administrator)
        self.Button_Quit.clicked.connect(Administrator.close)
        QtCore.QMetaObject.connectSlotsByName(Administrator)
        self.f = ''
        # 单次课时
        if (self.Course_Single_hours.currentText() == "单节"):
            self.single = 0
        elif (self.Course_Single_hours.currentText() == "半天"):
            self.single = 1
        else:
            self.single = 2

        # 连接数据库
        s = pymysql.connect("localhost", "root", "password", "cource_arranged_system")

        # 获取游标、数据
        cur = s.cursor()
        cur.execute("select * from courcelist;")
        # 数据列名
        col_lst = [tup[0] for tup in cur.description]
        font = QtGui.QFont('宋体', 10)
        self.Source_Table.horizontalHeader().setFont(font)
        self.Source_Table.setHorizontalHeaderLabels(col_lst)

        self.retranslateUi(Administrator)
        self.Button_Quit.clicked.connect(Administrator.close)
        self.Button_Cource_Require.clicked.connect(partial(self.event_Cource_Require, s, cur))
        self.Button_Course_Delete.clicked.connect(partial(self.event_Course_Delete, s, cur))
        self.Button_Course_Add.clicked.connect(partial(self.event_Course_Add, s, cur))
        self.Button_Course_Edit.clicked.connect(partial(self.event_Course_Edit, s, cur))
        self.Button_Add.clicked.connect(partial(self.event_Add, s, cur))
        self.Button_Delete.clicked.connect(partial(self.event_Delete, s, cur))
        self.Button_List_Create.clicked.connect(partial(self.event_Create, s, cur))
        self.Button_List_Require.clicked.connect(partial(self.event_requiretable))

    def retranslateUi(self, Administrator):
        _translate = QtCore.QCoreApplication.translate
        Administrator.setWindowTitle(_translate("Administrator", "排课系统"))
        self.Button_Cource_Require.setText(_translate("Administrator", "课程查询"))
        item = self.Source_Table.verticalHeaderItem(10)
        item.setText(_translate("Administrator", ""))
        item = self.Source_Table.horizontalHeaderItem(0)
        item.setText(_translate("Administrator", "名称"))
        item = self.Source_Table.horizontalHeaderItem(1)
        item.setText(_translate("Administrator", "课时"))
        item = self.Source_Table.horizontalHeaderItem(2)
        item.setText(_translate("Administrator", "教室"))
        item = self.Source_Table.horizontalHeaderItem(3)
        item.setText(_translate("Administrator", "教师"))
        item = self.Source_Table.horizontalHeaderItem(4)
        item.setText(_translate("Administrator", "专业"))
        item = self.Source_Table.horizontalHeaderItem(5)
        item.setText(_translate("Administrator", "类型"))
        item = self.Source_Table.horizontalHeaderItem(6)
        item.setText(_translate("Administrator", "单次课时"))
        item = self.Source_Table.horizontalHeaderItem(7)
        item.setText(_translate("Administrator", "开课时间"))
        item = self.Source_Table.horizontalHeaderItem(8)
        item.setText(_translate("Administrator", "结课时间"))
        self.label.setText(_translate("Administrator", "名称"))
        self.label_2.setText(_translate("Administrator", "课时"))
        self.label_3.setText(_translate("Administrator", "上课地点"))
        self.label_4.setText(_translate("Administrator", "教师"))
        self.label_5.setText(_translate("Administrator", "专业"))
        self.label_7.setText(_translate("Administrator", "开课日期"))
        self.label_8.setText(_translate("Administrator", "结课日期"))
        self.label_9.setText(_translate("Administrator", "单次课时"))
        self.Course_Single_hours.setItemText(0, _translate("Administrator", "单节"))
        self.Course_Single_hours.setItemText(1, _translate("Administrator", "半天"))
        self.Course_Single_hours.setItemText(2, _translate("Administrator", "全天"))
        self.Button_Course_Add.setText(_translate("Administrator", "添加课程"))
        self.Button_Course_Delete.setText(_translate("Administrator", "删除课程"))
        self.Button_Course_Edit.setText(_translate("Administrator", "修改课程"))
        self.Course_Type.setItemText(0, _translate("Administrator", "公共文化课"))
        self.Course_Type.setItemText(1, _translate("Administrator", "专业文化课"))
        self.Course_Type.setItemText(2, _translate("Administrator", "军事(体育)课"))
        self.Course_Type.setItemText(3, _translate("Administrator", "大项活动(节假日)"))
        self.label_10.setText(_translate("Administrator", "类型"))
        self.Course_Classroom.setItemText(0, _translate("Administrator", "室内"))
        self.Course_Classroom.setItemText(1, _translate("Administrator", "田径场"))
        self.Course_Classroom.setItemText(2, _translate("Administrator", "障碍场"))
        self.Button_Quit.setText(_translate("Administrator", "退出账户"))
        self.label_6.setText(_translate("Administrator", "欢迎登陆智能排课系统"))
        self.Button_Add.setText(_translate("Administrator", "添加"))
        self.Button_Delete.setText(_translate("Administrator", "删除"))
        self.Button_List_Create.setText(_translate("Administrator", "生成课表"))
        self.Button_List_Require.setText(_translate("Administrator", "查询课表"))
        self.Start_time.setPlaceholderText(_translate("Administrator", "开始日期：20190901"))
        self.End_time.setPlaceholderText(_translate("Administrator", "结束日期：20190901"))
        self.Course_Name.setPlaceholderText(_translate("Administrator", "如：高等数学"))
        self.Course_Teacher.setPlaceholderText(_translate("Administrator", "如：陈挚"))
        self.Course_Major.setPlaceholderText(_translate("Administrator", "如：软件工程"))
        self.Course_Start.setPlaceholderText(_translate("Administrator", "如：20190901"))
        self.Course_End.setPlaceholderText(_translate("Administrator", "如：20200117"))

        Buttonstyle = """
          QPushButton{font: 10pt "黑体"}
        """

        self.Button_List_Require.setStyleSheet(Buttonstyle)
        self.Button_List_Create.setStyleSheet(Buttonstyle)
        self.Button_Delete.setStyleSheet(Buttonstyle)
        self.Button_Add.setStyleSheet(Buttonstyle)
        self.Button_Course_Edit.setStyleSheet(Buttonstyle)
        self.Button_Course_Delete.setStyleSheet(Buttonstyle)
        self.Button_Cource_Require.setStyleSheet(Buttonstyle)
        self.Button_Course_Add.setStyleSheet(Buttonstyle)
        self.Button_Quit.setStyleSheet(Buttonstyle)
        self.Source_Table.setStyleSheet("QTableWidget{font: 10pt '黑体'}")

    # 课程查询
    def event_Cource_Require(self, s, cur):
        print("课程查询")
        tabledata = cur.fetchall()

        for i in range(len(tabledata)):
            for j in range(len(tabledata[0])):
                temp_data = tabledata[i][j]  # 临时记录，不能直接插入表格
                data1 = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                self.Source_Table.setItem(i, j, data1)

        # 添加至Course_List
        self.Course_Choose.clear()
        print("列表清空")
        cur.execute("select `名称` from courcelist;")
        tabledata = cur.fetchall()
        for i in range(len(tabledata)):
            temp_data = tabledata[i][0]  # 临时记录，不能直接插入表格
            self.Course_Choose.addItem(temp_data)
        print("Course_Choose更新")
        s.commit()

    # 添加课程
    def event_Course_Add(self, s, cur):
        # 类型转换
        data = []
        data.append(self.Course_Name.text())
        data.append(str(self.Course_hours.value()))
        data.append(self.Course_Classroom.currentText())
        data.append(self.Course_Teacher.text())
        data.append(self.Course_Major.text())
        data.append(self.Course_Type.currentText())
        data.append(str(self.single))
        data.append(self.Course_Start.text())
        data.append(self.Course_End.text())

        print(data)

        print("添加课程")
        sql = 'INSERT INTO courcelist VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        data = (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])
        cur.execute(sql, data)
        print(data[6])
        print("添加成功")

        cur.execute("select * from courcelist;")
        tabledata = cur.fetchall()
        for i in range(len(tabledata)):
            for j in range(len(tabledata[0])):
                temp_data = tabledata[i][j]  # 临时记录，不能直接插入表格
                data1 = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                self.Source_Table.setItem(i, j, data1)
        print("表格更新")

        # 添加至Course_List
        self.Course_Choose.clear()
        print("列表清空")
        cur.execute("select `名称` from courcelist;")
        tabledata = cur.fetchall()
        for i in range(len(tabledata)):
            temp_data = tabledata[i][0]  # 临时记录，不能直接插入表格
            self.Course_Choose.addItem(temp_data)
        print("Course_Choose更新")
        s.commit()


    # 删除课程
    def event_Course_Delete(self, s, cur):
        print("删除课程")
        data = self.Course_Name.text()
        cur.execute("DELETE FROM courcelist WHERE `名称` = %s;", data)
        print("删除成功")

        #更新表格
        self.Source_Table.clear()
        cur.execute("select * from courcelist;")
        col_lst = [tup[0] for tup in cur.description]
        self.Source_Table.setHorizontalHeaderLabels(col_lst)
        tabledata = cur.fetchall()
        for i in range(len(tabledata)):
            for j in range(len(tabledata[0])):
                temp_data = tabledata[i][j]  # 临时记录，不能直接插入表格
                data1 = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                self.Source_Table.setItem(i, j, data1)
        print("表格更新")

        # 添加至Course_List
        self.Course_Choose.clear()
        print("列表清空")
        cur.execute("select `名称` from courcelist;")
        tabledata = cur.fetchall()
        for i in range(len(tabledata)):
            temp_data = tabledata[i][0]  # 临时记录，不能直接插入表格
            self.Course_Choose.addItem(temp_data)
        print("Course_Choose更新")
        s.commit()

    # 修改课程
    def event_Course_Edit(self, s, cur):
        print("修改课程")
        data = self.Course_Name.text()
        cur.execute("DELETE FROM courcelist WHERE `名称` = %s;", data)
        # 类型转换
        data = []
        data.append(self.Course_Name.text())
        data.append(str(self.Course_hours.value()))
        data.append(self.Course_Classroom.currentText())
        data.append(self.Course_Teacher.text())
        data.append(self.Course_Major.text())
        data.append(self.Course_Type.currentText())
        data.append(str(self.single))
        data.append(self.Course_Start.text())
        data.append(self.Course_End.text())
        print(data)
        sql = 'INSERT INTO courcelist VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        data = (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])
        cur.execute(sql, data)
        print("修改成功")

        # 更新表格
        self.Source_Table.clear()
        cur.execute("select * from courcelist;")
        col_lst = [tup[0] for tup in cur.description]
        self.Source_Table.setHorizontalHeaderLabels(col_lst)
        tabledata = cur.fetchall()
        for i in range(len(tabledata)):
            for j in range(len(tabledata[0])):
                temp_data = tabledata[i][j]  # 临时记录，不能直接插入表格
                data1 = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                self.Source_Table.setItem(i, j, data1)
        print("表格更新")

        # 添加至Course_List
        self.Course_Choose.clear()
        print("列表清空")
        cur.execute("select `名称` from courcelist;")
        tabledata = cur.fetchall()
        for i in range(len(tabledata)):
            temp_data = tabledata[i][0]  # 临时记录，不能直接插入表格
            self.Course_Choose.addItem(temp_data)
        print("Course_Choose更新")
        s.commit()

    #添加至课表
    def event_Add(self, s, cur):
        data = self.Course_Choose.currentText()
        self.Course_List.addItem(data)

    #从课表删除
    def event_Delete(self, s, cur):
        data = self.Course_Choose.currentText()
        item = self.Course_List.findItems(data,Qt.MatchExactly)[0]
        self.f = self.Course_List.row(item)
        self.Course_List.takeItem(self.f)

    #生成课表
    def event_Create(self, s, cur):
        self.start_time = int(self.Start_time.text()) #开始时间
        print(self.start_time)
        self.end_time = int(self.End_time.text()) #结束时间
        print(self.end_time)

        # 计算星期
        date = self.Start_time.text()
        y = int(date[0:4])
        m = int(date[4:6])
        d = int(date[6:8])
        da = datetime.date(y, m, d)
        week = da.weekday() + 1
        self.start_day = week #开始星期
        print(self.start_day)

        #转移数据
        self.teacher = []
        self.cname = []
        self.major = []
        self.hours = []
        self.type = []
        self.single = []
        self.cstart = []
        self.cend = []
        self.cmajor = []
        self.cplace = []

        #选择要进入课表的课程
        cource = []
        for i in range(self.Course_List.count()):
            cource.append(self.Course_List.item(i).text())
        print(cource)

        cur.execute("select * from courcelist;")
        tabledata = cur.fetchall()
        for i in range(len(tabledata)):
            for j in range(len(tabledata[0])):
                temp_data = tabledata[i][j]  # 临时记录，不能直接插入表格
                flag = 0
                for m in cource:
                    if (m == tabledata[i][0]):
                        flag = 1
                if(flag):
                    if(j == 0):
                        self.cname.append(temp_data)
                    elif(j == 1):
                        self.hours.append(int(temp_data))
                    elif (j == 2):
                        self.cplace.append(temp_data)
                    elif (j == 3):
                        self.teacher.append(temp_data)
                    elif (j == 4):
                        self.major.append(temp_data)
                    elif (j == 5):
                        if(temp_data == '公共文化课' or temp_data == '专业文化课'):
                            self.type.append(2)
                        elif(temp_data == '军事(体育)课'):
                            self.type.append(1)
                        elif(temp_data == '大项活动(节假日)'):
                            self.type.append(0)
                    elif (j == 6):
                        self.single.append(int(temp_data))
                    elif (j == 7):
                        self.cstart.append(int(temp_data))
                    elif (j == 8):
                        self.cend.append(int(temp_data))

        for i in range(len(tabledata)):
            self.cmajor.append([tabledata[i][4]])
        '''
        print(self.teacher)
        print(self.cname)
        print(self.major)
        print(self.hours)
        print(self.type)
        print(self.single)
        print(self.cstart)
        print(self.cend)
        print(self.cmajor)
        print(self.cplace)
    '''


        a = give_timetable.cal(self.start_time,self.end_time,self.start_day,self.teacher,self.cname,self.major,self.hours,
                           self.type,self.single,self.cstart,self.cend,self.cmajor,self.cplace)['计算机科学与技术']
        print(a)
        self.date = []
        print("总日长：", len(a))
        for i in range(len(a)):
            delta = datetime.timedelta(days=i)
            self.date.append([str(delta + da)])

        d = 0
        for i in self.date:
            w = d // 7 + 1
            d = d+1
            i.append(w)
        print(len(self.date))
        for i in range(len(a)):
            for j in a[i]:
                self.date[i].append(j)
            self.date[i].append('')
        print(self.date)

        #建立数据库
        sql = """CREATE TABLE `CourceTable`  (
                `Date` varchar(255) NOT NULL,
                `Week` varchar(255) NULL,
                `First lesson` varchar(255) NULL,
                `Second lesson` varchar(255) NULL,
                `Third lesson` varchar(255) NULL,
                `Fourth lesson` varchar(255) NULL,
                `Fifth lesson` varchar(255) NULL,
                PRIMARY KEY (`Date`)
                );"""
        cur.execute("DROP TABLE IF EXISTS `CourceTable`")
        cur.execute(sql)
        cur.executemany("insert into `CourceTable` values(%s,%s,%s,%s,%s,%s,%s)",self.date)
        s.commit()

    #查询课表
    def event_requiretable(self):
        self.mainWindow = QMainWindow()
        ui = courcetable.creat_view()
        ui.__init__(self.mainWindow)
        self.mainWindow.show()



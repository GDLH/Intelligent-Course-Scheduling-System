# 导入包
import sys
import pymysql
from functools import partial
from PyQt5.Qt import QWidget
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QFrame, QApplication, QDialog, QDialogButtonBox,
                             QMessageBox, QVBoxLayout, QLineEdit, QTableWidgetItem, QTableWidget, QHBoxLayout)


# 建立界面类
class creat_view(QWidget):
    def __init__(self, parent=None):
        super(creat_view, self).__init__(parent)

        # 设置界面大小、名称、背景
        self.resize(1000, 1000)
        #self.minimumSize(1000,1000)
        #self.maximumSize(1000,1000)
        self.setWindowTitle('课程表')

        # 窗体属性
        self.setWindowFlags(Qt.Widget)

        # 连接数据库
        db = pymysql.connect("localhost", "root", "password", "cource_arranged_system")
        # 获取游标、数据
        cur = db.cursor()

        cur.execute("SELECT * FROM `CourceTable`")
        data = cur.fetchall()

        # 数据列名
        col_lst = [tup[0] for tup in cur.description]

        # 数据的大小
        row = len(data)
        vol = len(data[0])

        self.MyTable = QTableWidget(row, vol)
        font = QtGui.QFont('宋体', 10)

        # 设置字体、表头
        self.MyTable.horizontalHeader().setFont(font)
        self.MyTable.setHorizontalHeaderLabels(col_lst)
        # 设置竖直方向表头不可见
        self.MyTable.verticalHeader().setVisible(False)
        self.MyTable.setFrameShape(QFrame.NoFrame)

        # 构建表格插入数据
        for i in range(row):
            for j in range(vol):
                temp_data = data[i][j]  # 临时记录，不能直接插入表格
                data1 = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                self.MyTable.setItem(i, j, data1)

        # 垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.MyTable)
        self.setLayout(layout)







# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os

from PyQt5 import QtCore, QtGui, QtWidgets

from Util import unify_path


class Ui_Dialog(object):
    switch_window = QtCore.pyqtSignal()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 600)
        Dialog.setMinimumSize(QtCore.QSize(700, 600))
        Dialog.setBaseSize(QtCore.QSize(700, 600))
        self.User_label = QtWidgets.QLabel(Dialog)
        self.User_label.setGeometry(QtCore.QRect(190, 250, 61, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.User_label.setFont(font)
        self.User_label.setObjectName("User_label")
        self.password_label = QtWidgets.QLabel(Dialog)
        self.password_label.setGeometry(QtCore.QRect(190, 300, 61, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.login_button = QtWidgets.QPushButton(Dialog)
        self.login_button.setGeometry(QtCore.QRect(300, 370, 41, 41))

        # exe_path = os.path.dirname(os.path.abspath(sys.argv[0]))
        #生产环境使用这个代
        # exe_path= unify_path()[0]
        #开发环境使用这个代码
        exe_path= unify_path()


        button_path = os.path.join(exe_path, 'img/222.png')

        self.login_button.setStyleSheet(f"border-image:url({button_path});")

        self.login_button.setText("")
        self.login_button.setObjectName("login_button")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(140, 80, 411, 161))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(36)
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 440, 671, 41))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.background_listView = QtWidgets.QListView(Dialog)
        self.background_listView.setGeometry(QtCore.QRect(10, 0, 671, 800))
        self.background_listView.setMinimumSize(QtCore.QSize(0, 0))
        # self.background_listView.setStyleSheet("border-image:url(img/1111.png);")
        background_image_path = os.path.join(exe_path, 'img/1111.png')

        self.background_listView.setStyleSheet(f"border-image:url({background_image_path});")


        self.background_listView.setObjectName("background_listView")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(250, 300, 191, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 250, 191, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.background_listView.raise_()
        self.User_label.raise_()
        self.password_label.raise_()
        self.login_button.raise_()
        self.label_3.raise_()
        self.line.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "图像处理"))
        self.User_label.setText(_translate("Dialog", "账户"))
        self.password_label.setText(_translate("Dialog", "密码"))
        self.label_3.setText(_translate("Dialog", "图形算法批量处理平台"))

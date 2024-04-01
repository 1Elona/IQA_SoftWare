# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets

from util import Util


class Ui_Setting(object):
    switch_window = QtCore.pyqtSignal(tuple)
    algo = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)  # Adjusted window size
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Using a vertical layout for the central widget
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Defining the label for remarks
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setObjectName("label_19")
        self.label_19.setWordWrap(True)  # If you want the text to wrap when it's long
        self.verticalLayout.addWidget(self.label_19)

        # Space for adding dynamic content (widgets generated during runtime)
        self.vertiLayout_dynamicContent = QtWidgets.QVBoxLayout()
        self.vertiLayout_dynamicContent.setObjectName("vertiLayout_dynamicContent")
        self.verticalLayout.addLayout(self.vertiLayout_dynamicContent)

        # Push button to be added at the bottom
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.SettingToHome)
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout.setAlignment(self.pushButton, QtCore.Qt.AlignCenter)  # Center alignment for the button

        # Set central widget
        MainWindow.setCentralWidget(self.centralwidget)

        # Status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Translation and slot connections
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.radioButton_profession.setText(_translate("MainWindow", "专业模式"))
        self.label_19.setText(_translate("MainWindow", "备注：\n"
                                                       "井号后面为步长，可以用逗号分隔多组不同参数实验组\n"
                                                       "如图中表示阿尔法取值为1，2，3，5，5.2,5.4...6贝塔取2伽马取4，4.5 ...,9\n"
                                                       "德尔塔为4，则图中共产生3*5*1*10*1种不同的实验组"))
        self.pushButton.setText(_translate("MainWindow", "完成"))


    def SettingToHome(self):
        dic = {}
        #获取用户的输入值
        for i, (key_dict, value_dict) in zip(range(1, 1 + self.index_num), self.index_name.items()):
            lineedit = self.findChild(QtWidgets.QLineEdit, f"lineEdit_{i}")
            input = lineedit.text()
            dic[key_dict] = input
        self.switch_window.emit((dic,self.algo))

#从config中解析数据
    def init_index_by_config(self):
        data= Util.get_data_from_config(self.algo)
        info = Util.get_algorithm_params_info(data,self.algo)
        #某种算法的参数个数：
        self.index_num = info.length
        self.index_name = info.params #dict
        # 循环创建label和lineEdit
        # zip方法一次可以同时遍历一个列表和数组
        for i, (key_dict, value_dict) in zip(range(1,1+self.index_num), self.index_name.items()):
            layout = QtWidgets.QHBoxLayout()
            layout.setObjectName("horLayout_profession_"+str(i))
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++
            labelnew = QtWidgets.QLabel(key_dict)
            labelnew.setObjectName("label_"+str(i))
            #拿到这个新建的layout

            layout.addWidget(labelnew)
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++
            lineEdit = QtWidgets.QLineEdit()
            lineEdit.setObjectName("lineEdit_"+str(i))
            lineEdit.setPlaceholderText("取值范围:"+value_dict)
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++
            layout.addWidget(lineEdit)
            spacerItem7 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            layout.addItem(spacerItem7)
            self.vertiLayout_dynamicContent.addLayout(layout)











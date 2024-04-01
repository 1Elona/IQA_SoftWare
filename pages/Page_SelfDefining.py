# -*- coding: utf-8 -*-
import os
# Form implementation generated from reading ui file 'Page_SelfDefining.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton, QHeaderView, QTableWidgetItem

import util.Util
from util import Database
from util import Util

from pages.Page_Home import Ui_Home
class Ui_SelfDefining(object):
    choose_algo = ""
    alg_index_num = 3
    input_folder = ''
    output_folder = ''



    #SelfDefiningToHome
    switch_window = QtCore.pyqtSignal()
    #SelfDefiningToSetting
    switch_window_2 = QtCore.pyqtSignal(str)
    #SelfDefiningToIndex
    switch_window_3 = QtCore.pyqtSignal()
    #SelfDefiningToNewMainTask
    switch_window_4 = QtCore.pyqtSignal()
    #SelfDefiningToMoreParam
    switch_window_5 = QtCore.pyqtSignal()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1047, 734)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        # 这里的数量要和setItem的数量相匹配
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMinimumSize(QtCore.QSize(30, 26))
        self.label_4.setStyleSheet("image:url(:/新前缀/prompt.png)")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.setStretch(4, 30)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")


        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        li = ['序号', '算法名', '更多参数', '操作']
        j = 1
        for i in range(2, 2 + Ui_Home.num_columns):
            li.insert(i,str(f'p{j}'))
            j +=1
        self.tableWidget.setHorizontalHeaderLabels(li)

        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(3, item)
        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(329, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.Button_up_1 = QtWidgets.QPushButton(self.frame)
        self.Button_up_1.setObjectName("Button_up_1")
        self.horizontalLayout_4.addWidget(self.Button_up_1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setEnabled(True)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.Button_down_1 = QtWidgets.QPushButton(self.frame)
        self.Button_down_1.setObjectName("Button_down_1")
        self.horizontalLayout_4.addWidget(self.Button_down_1)
        spacerItem2 = QtWidgets.QSpacerItem(329, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        # self.pushButton = QtWidgets.QPushButton(self.frame)
        # self.pushButton.setObjectName("pushButton")
        # self.horizontalLayout_5.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1047, 42))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #完成
        self.pushButton_3.clicked.connect(self.SelfDefiningToHome)
        #算法设置
        self.pushButton_4.clicked.connect(self.SelfDefiningToSetting)
        #下一步
        self.pushButton_2.clicked.connect(self.SelfDefiningToIndex)

        # #上一步
        # self.pushButton.clicked.connect(self.SelfDefiningToNewMaintask)
        #

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "算法相关配置"))
        self.label_3.setText(_translate("MainWindow", "选择算法"))

        # 从config中读取算法名字
        for i,algname in enumerate(util.Util.get_algname_from_config()):
            self.comboBox.setItemText(i, _translate("MainWindow", algname))
        self.pushButton_4.setText(_translate("MainWindow", "算法设置"))
        # item = self.tableWidget.verticalHeaderItem(0)
        # item.setText(_translate("MainWindow", "新建行"))
        # item = self.tableWidget.verticalHeaderItem(1)
        # item.setText(_translate("MainWindow", "新建行"))
        # item = self.tableWidget.verticalHeaderItem(2)
        # item.setText(_translate("MainWindow", "新建行"))
        # item = self.tableWidget.horizontalHeaderItem(0)
        # item.setText(_translate("MainWindow", "新建列"))
        # item = self.tableWidget.horizontalHeaderItem(1)
        # item.setText(_translate("MainWindow", "新建列"))
        # item = self.tableWidget.horizontalHeaderItem(2)
        # item.setText(_translate("MainWindow", "新建列"))
        # item = self.tableWidget.horizontalHeaderItem(3)
        # item.setText(_translate("MainWindow", "新建列"))
        #
        self.Button_up_1.setText(_translate("MainWindow", "上一页"))
        self.label_2.setText(_translate("MainWindow", "1/5"))
        self.Button_down_1.setText(_translate("MainWindow", "下一页"))
        # self.pushButton.setText(_translate("MainWindow", "上一步"))
        self.pushButton_2.setText(_translate("MainWindow", "下一步"))
        self.pushButton_3.setText(_translate("MainWindow", "完成"))



    def SelfDefiningToHome(self):
        self.switch_window.emit()
    def SelfDefiningToSetting(self):
        self.switch_window_2.emit(self.comboBox.currentText())
    def SelfDefiningToIndex(self):
        self.switch_window_3.emit()
    # def SelfDefiningToNewMaintask(self):
    #     self.switch_window_4.emit()

    def add_task(self,row,dic,algoname):
        print("正在添加子任务中------")
        print("当前参数",dic)
        # {'alpha': {'data_1': [1, 2, 3], 'data_2': [5.0, 5.5]}, 'kernel_size': {'data_1': [1, 2, 3]},
        #  'iterations': {'data_1': [100, 150, 200, 250, 300]}}
        print("当前算法名",algoname) # EXAMPLE
        mainTask = Database.selectMaintaskByRow(row, Ui_Home.username)
        self.choose_algo = algoname
        self.alg_index_num = len(dic)
        #传入点击的行数
        id = mainTask['Id']



        #删除图标的按钮
        self.button_delete = QPushButton()
        self.pixmap = QPixmap("./iconfont/error.png")
        self.button_delete.setIcon(QtGui.QIcon(self.pixmap))
        # 按钮的大小
        self.button_delete.setIconSize(QSize(30, 30))
        self.button_delete.setMinimumSize(QSize(30, 30))
        self.button_delete.setMaximumSize(QSize(30, 30))
        # 按钮透明
        self.button_delete.setFlat(True)
        self.button_delete.setStyleSheet("background:transparent;")

        #更多图标的按钮
        self.button_more = QPushButton()
        self.pixmap = QPixmap("./iconfont/more.png")
        self.button_more.setIcon(QtGui.QIcon(self.pixmap))
        # 按钮的大小
        self.button_more.setIconSize(QSize(30, 30))
        self.button_more.setMinimumSize(QSize(30, 30))
        self.button_more.setMaximumSize(QSize(30, 30))
        # 按钮透明
        self.button_more.setFlat(True)
        self.button_more.setStyleSheet("background:transparent;")




        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 使表宽度自适应
        self.tableWidget.verticalHeader().setDefaultSectionSize(50) #使表高固定
        # 创建任务字典 这里需要自适应生成对应数量的参数列

        # for i in range(0, len(dic)):
        #     dictionary['p{}'.format(i + 1)] = ''

        #排列组合
        user_input = Util.crossjoin(dic)

        index = Database.create_SubTaskDatabase(user_input,Ui_Home.username,id)

        #[{'alpha': 1, 'kernel_size': 1, 'iterations': 100}, {'alpha': 1, 'kernel_size': 1, 'iterations': 150}, 。。。]
        #执行时间  #默认NULL
        execute_time = "NULL"
        #选择的指标 #还未添加该功能
        index_name = 'AMBE'

        # 更新表格
        row_count = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_count)
        self.tableWidget.setItem(row_count, 0,QTableWidgetItem(str(row_count+1)))
        #获取选择的算法名的值
        self.tableWidget.setItem(row_count, 1, QTableWidgetItem(self.comboBox.currentText()))

        # for i in range(0,Page_Home.Ui_Home.num_columns):#012
        #     dictionary[f'p{i+1}'] = random.randint(1,10)
        #     self.tableWidget.setItem(row_count, i+2,QTableWidgetItem(dictionary[f'p{i+1}']))
        #     user_input.append(dictionary[f'p{i+1}'])

        tk_name = mainTask['task_name']


        # 查出主任务原图文件夹有哪些图片
        print("主任务原图文件夹有哪些图片"+mainTask['input'])
        for file_name in os.listdir(mainTask['input']):
            for user_inputt in user_input:
                if Util.is_image_file(file_name):
                    Database.insert_SubTaskData(id,tk_name, Ui_Home.username,index,execute_time= execute_time, user_param_input_value = user_inputt,
                                                alg_name= self.comboBox.currentText(), ori_imgname=file_name, index_name= index_name
                                                )







        self.tableWidget.setCellWidget(row_count, 2+self.alg_index_num, self. button_more)
        self.tableWidget.setCellWidget(row_count, 3+self.alg_index_num, self.button_delete)


        self.button_delete.clicked.connect(self.delete_row)

        self.button_more.clicked.connect(self.more_p)




    def more_p(self):
        self.switch_window_5.emit()




    def delete_row(self):
        button = self.sender()
        row = self.tableWidget.indexAt(button.pos()).row()
        self.tableWidget.removeRow(row)


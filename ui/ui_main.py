# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(971, 562)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/o1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_image01 = QtWidgets.QLabel(self.centralwidget)
        self.label_image01.setFrameShape(QtWidgets.QFrame.Box)
        self.label_image01.setText("")
        self.label_image01.setScaledContents(True)
        self.label_image01.setObjectName("label_image01")
        self.verticalLayout.addWidget(self.label_image01)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_loadPicture01 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_loadPicture01.setObjectName("pushButton_loadPicture01")
        self.horizontalLayout.addWidget(self.pushButton_loadPicture01)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.label_show01 = QtWidgets.QLabel(self.centralwidget)
        self.label_show01.setFrameShape(QtWidgets.QFrame.Box)
        self.label_show01.setText("")
        self.label_show01.setObjectName("label_show01")
        self.verticalLayout_2.addWidget(self.label_show01)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_faceCompare = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_faceCompare.setFont(font)
        self.pushButton_faceCompare.setObjectName("pushButton_faceCompare")
        self.verticalLayout_7.addWidget(self.pushButton_faceCompare)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.verticalLayout_7.setStretch(2, 1)
        self.verticalLayout_7.setStretch(3, 4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_image02 = QtWidgets.QLabel(self.centralwidget)
        self.label_image02.setFrameShape(QtWidgets.QFrame.Box)
        self.label_image02.setText("")
        self.label_image02.setScaledContents(True)
        self.label_image02.setObjectName("label_image02")
        self.verticalLayout_5.addWidget(self.label_image02)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.pushButton_loadPicture02 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_loadPicture02.setFont(font)
        self.pushButton_loadPicture02.setObjectName("pushButton_loadPicture02")
        self.horizontalLayout_3.addWidget(self.pushButton_loadPicture02)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.label_show02 = QtWidgets.QLabel(self.centralwidget)
        self.label_show02.setFrameShape(QtWidgets.QFrame.Box)
        self.label_show02.setText("")
        self.label_show02.setObjectName("label_show02")
        self.verticalLayout_6.addWidget(self.label_show02)
        self.verticalLayout_6.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.verticalLayout_6)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_5.setStretch(0, 5)
        self.horizontalLayout_5.setStretch(1, 2)
        self.horizontalLayout_5.setStretch(2, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/image/o1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setObjectName("actionExit")
        self.actionabout = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/image/o2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionabout.setIcon(icon2)
        self.actionabout.setObjectName("actionabout")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "人脸识别演示程序"))
        self.pushButton_loadPicture01.setText(_translate("MainWindow", "载入图像"))
        self.label.setText(_translate("MainWindow", "人脸检测结果"))
        self.pushButton_faceCompare.setText(_translate("MainWindow", "人脸对比"))
        self.label_7.setText(_translate("MainWindow", "比对结果"))
        self.pushButton_loadPicture02.setText(_translate("MainWindow", "载入图像"))
        self.label_3.setText(_translate("MainWindow", "人脸检测结果"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionabout.setText(_translate("MainWindow", "about"))


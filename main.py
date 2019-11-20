# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys

#import cv2
from PyQt5.QtCore import QThread
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

import faceApi
from ui.ui_main import Ui_MainWindow
# import cv2
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from ui.ui_main import *


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

        self.label_image01.setScaledContents(True)  # 让图片自适应label大小
        self.label_image02.setScaledContents(True)

        self.pushButton_loadPicture01.clicked.connect(self.slot_load_picture01)
        self.pushButton_loadPicture02.clicked.connect(self.slot_load_picture02)
        self.pushButton_faceCompare.clicked.connect(self.slot_face_recognition)

    def slot_load_picture01(self):
        self.fileName01, filetype = QFileDialog.getOpenFileName(self,
                                                                "选取文件",
                                                                "./",
                                                                "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
        self.label_image01.setPixmap(QPixmap(self.fileName01))
        # thread=QThread().run()
        #
        # face = faceApi.FaceAPI()
        # results = face.face_detect(fileName01)
        #
        # img = cv2.imread(fileName01)
        # for face in results['result']['face_list']:
        #     text = face['face_token']
        #     location = face["location"]
        #     x1, y1 = int(location["left"]), int(location["top"])
        #     x2, y2 = int(location["left"] + location["width"]), int(location["top"] + location["height"])
        #     # print("截取出的文本为:", text)  # 画矩形框
        #     cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        #
        # # cv2.imwrite(fname[:-4] + "_result.jpg", img)
        # # 加载图片
        #
        # # 将图片转成BGRA模式;
        # img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
        # QtImg = QImage(img_rgb.data, img_rgb.shape[1], img_rgb.shape[0], QImage.Format_RGB32)
        # QtImg.show()
        # # 显示图片到label中;
        # self.label_image01.resize(QtCore.QSize(img_rgb.shape[1], img_rgb.shape[0]))
        # self.label_image01.setPixmap(QtGui.QPixmap.fromImage(QtImg))

    def slot_load_picture02(self):
        self.fileName02, filetype = QFileDialog.getOpenFileName(self,
                                                                "选取文件",
                                                                "./",
                                                                "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔

        self.label_image02.setPixmap(QPixmap(self.fileName02))

    def slot_face_recognition(self):
        face = faceApi.FaceAPI()
        result = face.face_match(self.fileName01, self.fileName02)
        score = int(result['result']['score'])
        print(result)
        if score > 90:
            self.label_show02.setText('比较像' + '\n得分：{%1}'.format(score))
        elif score > 60:
            self.label_show02.setText('不太像' + '\n得分：{%1}'.format(score))
        else:
            self.label_show02.setText('不像' + '\n得分：{%1}'.format(score))
        # QMessageBox.about(self, '登陆', '请输入姓名')


# words_results = client.general(image)
# results = words_results["words_result"]
#
# img = cv2.imread(fname)
# for result in results:
#     text = result["words"]
#     location = result["location"]
#
#     print("截取出的文本为:",text)   # 画矩形框
#     cv2.rectangle(img, (location["left"],location["top"]), (location["left"]+location["width"],location["top"]+location["height"]), (0,255,0), 2)
#
# cv2.imwrite(fname[:-4]+"_result.jpg", img)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MyWindow()
    mainWindow.show()
    sys.exit(app.exec_())

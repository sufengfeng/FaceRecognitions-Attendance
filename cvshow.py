from aip import AipFace
import cv2
import faceApi

fname = r'C:\Users\Administrator.SC-201911172258\PycharmProjects\FaceRecognition\testface\1421221304095989.jpg'
face = faceApi.FaceAPI()
results = face.face_detect(fname)

img = cv2.imread(fname)

for face in results['result']['face_list']:
    text = face['face_token']
    location = face["location"]
    x1, y1 =int(location["left"]), int(location["top"])
    x2, y2= int(location["left"] + location["width"]), int(location["top"] + location["height"])

    print("截取出的文本为:", text)  # 画矩形框
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

#cv2.imwrite(fname[:-4] + "_result.jpg", img)
# 加载图片

from PyQt5.QtGui import *
# 将图片转成BGRA模式;
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
QtImg = QImage(img_rgb.data, img_rgb.shape[1], img_rgb.shape[0], QImage.Format_RGB32)
# 显示图片到label中;
labImage.resize(QtCore.QSize(img_rgb.shape[1], img_rgb.shape[0]))
labImage.setPixmap(QtGui.QPixmap.fromImage(QtImg))


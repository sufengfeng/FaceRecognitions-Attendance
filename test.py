# -*- coding: UTF-8 -*-

from aip import AipFace
# import cv2
# import matplotlib.pyplot as plt

# 定义常量
APP_ID = '9851066'
API_KEY = 'LUGBatgyRGoerR9FZbV4SQYk'
SECRET_KEY = 'fB2MNz1c2UHLTximFlC4laXPg7CVfyjV'

# 初始化AipFace对象
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
filePath = r'E:\testface\timg.jpg'


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

        # 定义参数变量


options = {
    'max_face_num': 1, # 图像数量
    'face_fields': "age,beauty,expression,faceshape",
}
# 调用人脸属性检测接口
result = aipFace.detect(get_file_content(filePath), options)

# print(result)
# print(type(result))

# 解析位置信息
location=result['result'][0]['location']
left_top=(location['left'],location['top'])
right_bottom=(left_top[0]+location['width'],left_top[1]+location['height'])

# img=cv2.imread(filePath)
# cv2.rectangle(img,left_top,right_bottom,(0,0,255),2)
#
# cv2.imshow('img',img)
# cv2.waitKey(0)
# plt.imshow(img,"gray")
# plt.show()

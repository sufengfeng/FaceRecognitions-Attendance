# -*-coding:UTF-8-*-
from aip import AipFace
import base64


def imgToBase64(fileName):
    with open(fileName, 'rb')as f:
        data = f.read()
        base64Bytes = base64.b64encode(data)
        return str(base64Bytes, 'utf-8')


class FaceAPI:
    """ 你的 APPID AK SK """
    APP_ID = '17809644'
    API_KEY = 'vlN74XYryBmSChGrytjkejqZ'
    SECRET_KEY = 'Z8NDrLKk53mCeB85PO2Z4STQFNeZ92ok'

    def __init__(self):
        # 初始化AipFace对象
        self.client = AipFace(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    # 人脸检测
    def face_detect(self, fileName):
        image = imgToBase64(fileName)
        imageType = "BASE64"
        """ 如果有可选参数 """
        options = {}
        options["face_field"] = "age"
        options["max_face_num"] = 2
        options["face_type"] = "LIVE"
        options["liveness_control"] = "LOW"

        """ 带参数调用人脸检测 """
        result = self.client.detect(image, imageType, options)
        return result

    # 图片匹配
    def face_match(self, picPathName01, picPathName02):
        result = self.client.match([
            {
                'image': imgToBase64(picPathName01),
                'image_type': 'BASE64',
            },
            {
                'image': imgToBase64(picPathName02),
                'image_type': 'BASE64',
            }
        ])
        return result

    # 活体检测
    def face_verify(self, picPathName01, picPathName02):
        result = self.client.faceverify([
            {
                'image': imgToBase64(picPathName01),
                'image_type': 'BASE64',
            },
            {
                'image': imgToBase64(picPathName02),
                'image_type': 'BASE64',
            }
        ])
        return result


if __name__ == "__main__":
    face = FaceAPI()
    result = face.face_detect(
        r'C:\Users\Administrator.SC-201911172258\PycharmProjects\FaceRecognition\testface\1421221304095989.jpg')
    print(result)
    result = face.face_match(
        r'C:\Users\Administrator.SC-201911172258\PycharmProjects\FaceRecognition\testface\timg.jpg',
        r'C:\Users\Administrator.SC-201911172258\PycharmProjects\FaceRecognition\testface\timg1.jpg')
    print(result)
    result = face.face_verify(
        r'C:\Users\Administrator.SC-201911172258\PycharmProjects\FaceRecognition\testface\timg.jpg',
        r'C:\Users\Administrator.SC-201911172258\PycharmProjects\FaceRecognition\testface\timg1.jpg')
    print(result)

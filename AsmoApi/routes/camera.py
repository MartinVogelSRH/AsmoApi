import web
import time
from io import BytesIO
from controller.camera import Camera as CameraController
try:
    import picamera
    GPIOAvailable = True
except:
    GPIOAvailable = False

class Camera(object):
    """description of class"""
    def GET(self):
        return 'please use this API with /SinglePicture or /Stream'
    def getOneWithHelper(self):
        web.header('Content-type','image/jpg')
        return CameraController().get_frame()

    def GET(self,name):
        if name == 'SinglePicture':
            yield self.getOneWithHelper()
        elif name =='Stream':
            web.header('Content-type','multipart/x-mixed-replace; boundary=frame')
            web.header('Transfer-Encoding','chunked') 
            while True:
                frame = CameraController().get_frame()
                yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        else:
            yield 'please use this API with /SinglePicture or /Stream'
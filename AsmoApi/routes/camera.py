import web
import time
from io import BytesIO
from controller.cameraHelper import CameraHelper

try:
    import picamera
    GPIOAvailable = True
except:
    GPIOAvailable = False

class Camera(object):
    """description of class"""
    def GET(self):
        if GPIOAvailable:
            web.header('Content-type','video/mp4')
            #web.header('mimetype', 'multipart/x-mixed-replace; boundary=frame')
            web.header('Transfer-Encoding','chunked') 
            starttime = time.time()
            while True:
                frame = CameraHelper().get_frame()
                yield frame
            #for foo in cam.capture_continuous(stream, 'jpeg'):
            #    stream.seek(0)
            #    #time.sleep(1)
            #    image = Image.open(stream)
            #    stream.seek(0)
            #    stream.truncate()
            #    yield image.tobytes()
                #yield (b'--frame\r\n' b'Content-Type: video/mp4\r\n\r\n' + image.tobytes() + b'\r\n\r\n')
                #yield stream.read()

                #web.seeother('../static/current.jpg')
#app.route('/pic').post(pic.makePic);

    def getOne():
        if GPIOAvailable:
            stream = BytesIO()
            cam = picamera.PiCamera()
            cam.resolution = (640, 480)
            web.header('Content-type','image/jpg')
            web.header('Transfer-Encoding','chunked') 
            cam.start_preview()
            time.sleep(2)
            cam.capture(stream, format='jpeg')
            #cam.capture('/home/pi/Asmo/AsmoApi/AsmoApi/static/current.jpg')
            cam.close()
            stream.seek(0)
            #image = Image.open(stream)
            return stream
            #web.seeother('../static/current.jpg')

    def getOneWithHelper(self):
        if GPIOAvailable:
            web.header('Content-type','image/jpg')
            yield CameraHelper().get_frame();
    def GET(self,name):
        if name == 'SinglePic':
            yield self.getOneWithHelper()
        elif name =='Stream':
            web.header('Content-type','video/mp4')
            web.header('Transfer-Encoding','chunked') 
            while True:
                frame = CameraHelper().get_frame()
                yield frame
        else:
            yield 'undefined'
import web
import time
from io import BytesIO
from PIL import Image
try:
    import picamera
    GPIOAvailable = True
except:
    GPIOAvailable = False

class Camera(object):
    """description of class"""
    def GET(self):
        if GPIOAvailable:
            stream = BytesIO()
            cam = picamera.PiCamera()
            cam.resolution = (640, 480)
            web.header('Content-type','video/mp4')
            web.header('Transfer-Encoding','chunked') 
            cam.start_preview()
            time.sleep(2)
            for foo in cam.capture_continuous(stream, 'jpeg', use_video_port=True):
                stream.seek(0)
                #time.sleep(1)
                #image = Image.open(stream)
                yield stream.read()
                #web.seeother('../static/current.jpg')
#app.route('/pic').post(pic.makePic);

    def getone():
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
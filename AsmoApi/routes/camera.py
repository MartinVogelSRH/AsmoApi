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
            web.header('Content-type','image/jpg')
            cam.start_preview()
            time.sleep(2)
            camera.capture(stream, format='jpeg')
            #cam.capture('/home/pi/Asmo/AsmoApi/AsmoApi/static/current.jpg')
            cam.close()
            stream.seek(0)
            image = Image.open(stream)
            return image
            #web.seeother('../static/current.jpg')
#app.route('/pic').post(pic.makePic);
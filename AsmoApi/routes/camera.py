import web
import time
from io import BytesIO
try:
    import picamera
    GPIOAvailable = True
except:
    GPIOAvailable = False

class Camera(object):
    """description of class"""
    def GET(self):
        if GPIOAvailable:
            cam = picamera.PiCamera()
            cam.resolution = (640, 480)
            #web.header('Content-type','image/jpg')
            cam.start_preview()
            time.sleep(2)
            cam.capture('../static/current.jpg')
            web.seeother('../static/current.jpg')
#app.route('/pic').post(pic.makePic);
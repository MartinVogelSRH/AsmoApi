import web

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
            web.header('Content-type','multipart/x-mixed-replace; boundary=--jpgboundary')
            web.header('Transfer-Encoding','chunked')
            while True:
                frame = camera.get_frame()
                yield frame
        
#app.route('/pic').post(pic.makePic);
import web

try:
    import picamera
    GPIOAvailable = True
except:
    GPIOAvailable = False


def getDistance():
    if GPIOAvailable:
        camera = picamera.Camera()
        return 'Test'
    else:
        return "Not running on a pi or picamera library not installed"
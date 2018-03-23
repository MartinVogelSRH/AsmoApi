import web
from routes.distance import Distance
from routes.index import Index
from routes.led import Led
from routes.motor import Motor
from routes.camera import Camera
from routes.temperature import Temperature
from routes.shutdown import Shutdown
from routes.favicon import Favicon
import controller.led
import atexit

PossibleUrls = (
                '/api/motor', 'Motor',
                '/api/distance', 'Distance',
                '/api/camera',  'Camera',
                '/api/camera/(.*)',  'Camera',
                '/api/led', 'Led',
                '/api/temperature', 'Temperature',
                '/api/shutdown', 'Shutdown',
                '/favicon.ico', 'Favicon',
                '/(.*)', 'Index',
                '/', 'Index'
)

def cleaning():
    print('cleanup')
    try:
        import RPi.GPIO as GPIO
        GPIO.cleanup()
    except:
        print('nothing')

if __name__ == "__main__":
    atexit.register(cleaning)
    controller.led.toogleAllOff()
    controller.led.toogleColor('green')
    Server = web.application(PossibleUrls,globals())
    try:
        Server.run()
    except Exception as e:
        print('An Error occurred:\n' + str(e))
        controller.led.toogleAllOff()
        controller.led.toogleColor('red')


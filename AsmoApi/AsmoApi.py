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

if __name__ == "__main__":
    Server = web.application(PossibleUrls,globals())
    Server.run()
    controller.led.toogleColor('green')
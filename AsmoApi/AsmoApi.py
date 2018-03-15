import web
from routes.distance import Distance
from routes.index import Index
from routes.led import Led
from routes.motor import Motor
from routes.picture import Picture
from routes.temperature import Temperature
from routes.shutdown import Shutdown



PossibleUrls = (
                '/api/motor', 'Motor',
                '/api/distance', 'Distance',
                '/api/picture',  'Picture',
                '/api/led', 'Led',
                '/api/temperature', 'Temperature',
                '/api/shutdown', 'Shutdown',
                '/(.*)', 'Index',
                '/', 'Index'
)
Server = web.application(PossibleUrls,globals())
if __name__ == "__main__":
    Server.run()
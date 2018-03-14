import json
import controller.led
import web

class Led(object):
    """description of class"""
    def GET(self):
        return controller.led.toogleAllOff()
    def POST(self):
        data = json.loads(web.data())
        return controller.led.toogleColor(data['color'])
#app.route('/led')
#        .post(led.toggleLed)
#        .get(led.turnOff);
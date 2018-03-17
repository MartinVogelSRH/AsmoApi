import json
import controller.led
import web

class Led(object):
    """description of class"""
    def GET(self):
        dictToReturn = {'message': controller.led.toogleAllOff()}
        web.header('Content-Type', 'application/json')
        return json.dumps(dictToReturn)
    def POST(self):
        data = json.loads(web.data())
        dictToReturn = {'message': controller.led.toogleColor(data['color'])}
        web.header('Content-Type', 'application/json')
        return json.dumps(dictToReturn)
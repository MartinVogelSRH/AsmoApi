import controller.distance
import json
import web

class Distance(object):
    """description of class"""
    def GET(self):
        dictToReturn = {'distance': controller.distance.getDistance()}
        web.header('Content-Type', 'application/json')
        return json.dumps(dictToReturn)
from controller.distance import DistanceController
import json
import web

class Distance(object):
    """description of class"""
    def GET(self):
        dictToReturn = {'distance': DistanceController().getDistance()}
        web.header('Content-Type', 'application/json')
        return json.dumps(dictToReturn)
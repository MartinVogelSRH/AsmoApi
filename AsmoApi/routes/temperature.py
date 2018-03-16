import controller.temperature

class Temperature(object):
    """description of class"""
    def GET(self):
        dictToReturn = {'message': controller.temperature.getTempAndHum()}
        web.header('Content-Type', 'application/json')
        return json.dumps(dictToReturn)

#app.route('/temp').get(temp.get);
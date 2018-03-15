import controller.temperature

class Temperature(object):
    """description of class"""
    def GET(self):
        return controller.temperature.getTempAndHum()

#app.route('/temp').get(temp.get);
import controller.led
class Led(object):
    """description of class"""
    def GET(self):
        return controller.led.toogleAllOff()

#app.route('/led')
#        .post(led.toggleLed)
#        .get(led.turnOff);
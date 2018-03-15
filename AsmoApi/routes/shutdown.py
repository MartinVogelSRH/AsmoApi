import os

class Shutdown(object):
    """description of class"""
    def GET(self):
        os.system ('sudo shutdown --poweroff now')
#app.route('/led')
#        .post(led.toggleLed)
#        .get(led.turnOff);

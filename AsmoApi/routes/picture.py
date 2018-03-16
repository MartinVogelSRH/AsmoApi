import web
class Picture(object):
    """description of class"""

    def GET(self):
        raise web.seeother('/static/test.jpg')
#app.route('/pic').post(pic.makePic);
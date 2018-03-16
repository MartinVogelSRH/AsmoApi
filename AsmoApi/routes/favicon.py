import web



class Favicon(object):
    """description of class"""

    def GET(self):
        raise web.seeother('static/favicon.ico')
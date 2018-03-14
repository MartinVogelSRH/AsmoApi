import web



class Index(object):
    """description of class"""

    def GET(self, file=None):
        if file != '':
            htmlPage = web.template.frender('views/' + file)
            return htmlPage()
            #renderer = web.template.render("views")
            #return renderer.index()
        raise web.seeother('/index.html')
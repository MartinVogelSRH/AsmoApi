import controller.distance

class Distance(object):
    """description of class"""
    def GET(self):
        return controller.distance.getDistance()
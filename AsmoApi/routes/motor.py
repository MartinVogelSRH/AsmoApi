import web
import controller.motor

class Motor(object):
    """description of class"""

    def GET(self):
        dictToReturn = {'message': 'please use this as a post function and post motor1 and motor2 as form data'}
        web.header('Content-Type', 'application/json')
        return json.dumps(dictToReturn)
    def POST(self):
        inputData = web.input()
        motor1speed, motor2speed = inputData.motor1, inputData.motor2
        dictToReturn = {'message': controller.motor.setMotors(motor1speed, motor2speed)}
        web.header('Content-Type', 'application/json')
        return json.dumps(dictToReturn)
    #app.route('/motor').post(motor.setMotorSequenz);
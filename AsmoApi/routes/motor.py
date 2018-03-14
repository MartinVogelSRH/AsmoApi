import web
import controller.motor

class Motor(object):
    """description of class"""

    def GET(self):
        return "Hallo"
    def POST(self):
        inputData = web.input()
        motor1speed, motor2speed = inputData.motor1, inputData.motor2
        return controller.motor.setMotors(motor1speed, motor2speed)
    #app.route('/motor').post(motor.setMotorSequenz);
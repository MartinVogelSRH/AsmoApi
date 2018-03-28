import controller.distance
try:
    import RPi.GPIO as GPIO
    import controller.PicoBorgRev
    GPIOAvailable = True
except:
    GPIOAvailable = False

if GPIOAvailable:
    PBR1 = controller.PicoBorgRev.PicoBorgRev()
    PBR1.Init()

def setMotors (motor1speed = 0, motor2speed = 0):
    
    motor1speed = float(motor1speed)
    motor2speed = float(motor2speed)
    if abs(motor1speed) > 1:
        motor1speed = motor1speed / float(100)
    if abs(motor2speed) > 1:
        motor2speed = motor2speed / float(100)
    if GPIOAvailable:
        PBR1.SetMotor1(motor1speed)
        PBR1.SetMotor2(motor2speed)
        controller.distance.DistanceController().getDistance() #starting the read of distances. This will stop the motor if the distance is too low.
        return "Success"
    else:
        print("not running on a pi. Motor 1 would have been set to: " + str(motor1speed) + " Motor 2 would have been set to: " + str(motor2speed))
        return "not running on a pi. Motor 1 would have been set to: " + str(motor1speed) + " Motor 2 would have been set to: " + str(motor2speed)

def getMotors():
    motor1speed = PBR1.GetMotor1()
    motor2speed = PBR1.GetMotor2()
    return motor1speed,motor2speed